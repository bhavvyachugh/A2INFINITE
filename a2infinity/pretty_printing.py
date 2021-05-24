#######################################################
# Pretty printing object and sql by various means
#######################################################

#######################
#FUNCTIONS
######################
def anything(var,trace):
    trace_hightligh = pp_traceback(trace)
    str3 = '\n\n'.join([str(var), trace_hightligh])
    return str3

# The below function converts any byte string keys into string
#we found that if key is byte string then json.dumps will throw error So we have to convert the dict
# recursive key as string conversion for byte keys
#https://stackoverflow.com/a/57014404/2897115
def keys_string(d):
    rval = {}

    # Sometimes the object is not a dict it can be list and also. So 
    # Eg:
    ## '_preconf_set_by_auto': {'result_backend', 'broker_url'}
    ## the above will raise error: AttributeError: 'str' object has no attribute 'items'
    ## list = [1,3,4] To declare a tuple, we use brackets.
    ## tuples = (1, 2, "a") To declare a tuple, we use parentheses.
    ## sets = {1,2,3} declare a set. Use curly braces 
    # So we check whether its a dict and then its a tuple,list,set
    if not isinstance(d, dict):
        if isinstance(d,(tuple,list,set)):
            v = [keys_string(x) for x in d]
            return v
        else:
            return d

    # we have to store the keys in a list else some objects give dictionary
    # changed size during iteration error
    # https://stackoverflow.com/questions/59662479/python-error-dictionary-changed-size-during-iteration-when-trying-to-iterate
    keys = list(d.keys())
    for k in keys:
        v = d[k]
        if isinstance(k,bytes):
            k = k.decode()
        if isinstance(v,dict):
            v = keys_string(v)
        elif isinstance(v,(tuple,list,set)):
            v = [keys_string(x) for x in v]
        rval[k] = v
    return rval


# in json_dumps we can pass a default function
def json_dumps_default(obj):
    repr_obj = repr(obj)
    str_obj = str(obj)

    if repr_obj == str_obj:
        return repr_obj
    else:
        return repr_obj,f"STR: {str_obj}"

# If the obj is not dict.tuple,list,set then we categorize the dir(obj)
def pp_odir_getobject(obj):
    if isinstance(obj,dict):
        return keys_string(obj)
    if isinstance(obj,(tuple,list,set)):
        return keys_string(obj)

    #c_dict = {k: getattr(obj, k) for k in dir(obj)} # this gives all the properties listed using dir(c)

    # we are not using the above is because if there are except it stops
    c_dict = {
                '00_METHODS********************************************************************************':{},
                "01_UNDESCORE******************************************************************************":{},
                "02_OTHERS*********************************************************************************":{},
                "03_EXCEPTIONS*****************************************************************************":{},
                }
    for key in dir(obj):
        try:
            attr_obj = getattr(obj, key)
            if callable(attr_obj):
            #if inspect.ismethod(attr_obj):
                c_dict['00_METHODS********************************************************************************'][key] = attr_obj
            else:
                if key.startswith("_"):
                    c_dict['01_UNDESCORE******************************************************************************'][key] = attr_obj
                else:
                    c_dict['02_OTHERS*********************************************************************************'][key] = attr_obj
        except Exception as x:
            c_dict['03_EXCEPTIONS*****************************************************************************'][key] = x
    return keys_string(c_dict)


# pretty print using dir(obj) and then its properties and also the traceback
def dumps(obj):

    ##  json.dumps(queryset) in Jupyter runs lot of sqls if the object is query set so we want to avoid that. It work fine with views.py
    ## .So we want to stop logging before json_str and continue back with its state after
    import logging
    logger_database = logging.getLogger("django.db.backends")
    try:
        log_filt_state=logger_database.filters[0].state
        logger_database.filters[0].close()
    except:
        pass

    # we have to do two things 1) is to convert any byte strings to keys and also segrate into methods,underscore and other and exceptions
    c_dict_flattened = pp_odir_getobject(obj)

    import json
    from pygments import highlight
    from pygments.lexers import JsonLexer
    from pygments.formatters import TerminalTrueColorFormatter
    #Before passing the dict we want to avoid any byte string keys so keys_string(c_dict)
    json_str=json.dumps(c_dict_flattened, indent=4, sort_keys=True, default=json_dumps_default)

    try:
        # based on the logging status continue after    
        if log_filt_state == 'open':
            logger_database.filters[0].open()
    except:
        pass

    return json_str


#######################################################
# Get ip address
#######################################################

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip