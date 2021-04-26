import os
import logging
import traceback
import json

DEBUG=True


ALLOWED_HOSTS = ["*"]


MIDDLEWARE = [
    'a2infinity.external_config.custom_middleware.request_exposure.RequestExposerMiddleware', #<--- will set the exposed_request  variable, initiall define it as None
    'a2infinity.external_config.custom_middleware.request_logging.middleware.LoggingMiddleware', #<--- Added install djang-request-logging
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

exposed_request=[] # will be set by 'api.custom_middleware.request_exposure.RequestExposerMiddleware'

class VerFormatter2(logging.Formatter):
    def format(self, record):
        #add new attributes to record which will be used later
        # we also want to have the url requested and its method
        record.absolute_path = json.dumps(exposed_request,default=str,indent=4)
        record.topline = "--------------------------------------------------------------------------------------------------------------"
        record.botline = "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
        return super(VerFormatter2, self).format(record)


__file__ = "/home/web_dev/freelancer/food_delivery/FoodDelivery/api/api/settings.py"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECT_PATH=BASE_DIR


# Verbose formatter to be used for the handler used in logging "custom_string"
class VerFormatter(logging.Formatter):
    def format(self, record):
        ## We want to show some code lines while logging. So that its eays to know 
        #create a list of all the linenumber: lines 
        lines=[]
        string = ""
        file = record.pathname
        line = record.lineno
        if os.path.exists(file):
            line -= 1
            with open(file,"r") as f:
                rl = f.readlines()
                tblines = rl[max(line-5,0):min(line+3,len(rl))]
                # read 2 lines before and 2 lines after
                for i,tl in enumerate(tblines):
                    tl = tl.rstrip()

                    if i==5:
                        string = string + " =====> "+str(line+1+i-5)+":  "+tl+" <====\n"
                    elif tl:
                        string = string + "        "+str(line+1+i-5)+":  "+tl+"\n"


        # colorize the code
        import pygments
        from pygments.lexers.python import Python3Lexer
        from pygments.formatters import TerminalTrueColorFormatter
        # windows terminal has no colors
        #code = pygments.highlight(
        #    code,
        #    Python3Lexer(),
        #    #TerminalTrueColorFormatter(style='monokai') #use for terminal
        #    TerminalTrueColorFormatter() #use for jupyter notebook
        #)

        #add new attributes to record which will be used later
        # we also want to have the url requested and its method
        record.absolute_path = json.dumps(exposed_request,default=str,indent=4)
        record.codelines = string
        record.topline = "--------------------------------------------------------------------------------------------------------------"
        record.botline = "--------------------------------------------------------------------------------------------------------------"
        return super(VerFormatter, self).format(record)



# SQL formatter to be used for the handler used in logging "django.db.backends"
class SQLFormatter(logging.Formatter):
    local_request = None
    def format(self, record):

        # Check if Pygments is available for coloring 
        try:
            import pygments
            from pygments.lexers import SqlLexer
            from pygments.formatters import TerminalTrueColorFormatter
        except ImportError:
            pygments = None

        # Check if sqlparse is available for indentation
        try:
            import sqlparse
        except ImportError:
            sqlparse = None

        # Remove leading and trailing whitespaces
        sql = record.sql.strip()

        if sqlparse:
            # Indent the SQL query
            sql = sqlparse.format(sql, reindent=True)

        import traceback
        import re
        tracearray = traceback.extract_stack()
        
        filepath = PROJECT_PATH
        filepath_dont = os.path.abspath(f"{PROJECT_PATH}/../.venv")
        filepath1 = os.path.abspath(f"{PROJECT_PATH}/../../.venv/lib/python3.7/site-packages/rest_auth/")
        filepath2 = os.path.abspath(f"{PROJECT_PATH}/../../.venv/lib/python3.7/site-packages/allauth/")
        filepath3 = os.path.abspath(f"{PROJECT_PATH}/../../.venv/lib/python3.7/site-packages/django/contrib/auth/")
        filepath4 = os.path.abspath(f"{PROJECT_PATH}/../../.venv/lib/python3.7/site-packages/rest_framework/authentication")
        

#        #matches = [i for i in tracearray if (re.search(rf"{filepath}", i) and not re.search(rf"{filepath_dont}", i)) ]
#        for i in range(0,len(tracearray)):
#            if (re.search(rf"{filepath}", tracearray[i]) or re.search(rf"{filepath1}", tracearray[i]) or re.search(rf"{filepath2}", tracearray[i])):
#                tracearray[i] = f"{i}***{tracearray[i]}"
#            else:
#                tracearray[i] = f"{i}{tracearray[i]}"

        matches2 = [i for i in tracearray if (re.search(rf"{filepath}", i[0]) or re.search(rf"{filepath1}", i[0]) or re.search(rf"{filepath2}", i[0]) or re.search(rf"{filepath3}", i[0]) or re.search(rf"{filepath4}", i[0]))]
        #matches2 = tracearray


        matches=[]
        for file,line,w1,w2 in matches2[:-1]:
            string = ""
            string = string + '->File "{}", line {}, in {}\n'.format(file,line,w1)
            if os.path.exists(file):
                line -= 1
                with open(file,"r") as f:
                    rl = f.readlines()
                    tblines = rl[max(line-5,0):min(line+3,len(rl))]
                    # read 2 lines before and 2 lines after
                    for i,tl in enumerate(tblines):
                        tl = tl.rstrip()

                        if i==5:
                            string = string + " =====> "+str(line+1+i-5)+":  "+tl+" <====\n"
                        elif tl:
                            string = string + "        "+str(line+1+i-5)+":  "+tl+"\n"
            matches.append(string)


        record.traceback = ''.join(matches)


        # Set the record's statement to the formatted query
        record.statement = sql
        if 'duration' in record.__dict__:
          pass
        else:
          record.duration = "NA"

        #record.absolute_path = json.dumps(exposed_request,default=str,indent=4)
        record.absolute_path = exposed_request
        record.topline = "--------------------------------------------------------------------------------------------------------------"
        record.botline = "--------------------------------------------------------------------------------------------------------------"

        return super(SQLFormatter, self).format(record)


### Change this to closed when there are too many queries going on.and use 
### logger_database.filters[0].open() INDSIDE THE views function not on the top
LoggerGate_Default_State="open"  # use this if we want to see all the sql
#LoggerGate_Default_State="closed"  # use this if we want dont want to see all the sql


# Filter class to stop or start logging for "django.db.backends"
class LoggerGate:
    def __init__(self, state=LoggerGate_Default_State):
        # We found that the settings.py runs twice and the filters are created twice. So we have to keep only one. So we delete all the previous filters before we create the new one
        import logging
        logger_database = logging.getLogger("django.db.backends")
        try:
            for filter in logger_database.filters:
                logger_database.removeFilter(filter)
        except Exception as e:
            pass
        self.state = state

    def open(self):
        self.state = 'open'

    def close(self):
        self.state = 'closed'

    def filter(self, record):
        """
        Determine if the specified record is to be logged.

        Is the specified record to be logged? Returns 0/False for no, nonzero/True for
        yes. If deemed appropriate, the record may be modified in-place.
        """
        return self.state == 'open'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            '()': VerFormatter,
            'format': '%(topline)s\n%(asctime)s\nXXX%(levelname)sXXX %(funcName)s() %(pathname)s[:%(lineno)s] %(name)s\n%(absolute_path)s\n%(topline)s\n\n%(codelines)s\n\n%(message)s\n\n%(codelines)s',
            #'datefmt': "[%d/%b/%Y %H:%M:%S %p %Z]"
        },
        'simple': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
        'sql': {
            '()': SQLFormatter,
            'format': '%(topline)s\n%(asctime)s\nXXX%(levelname)sXXX %(funcName)s() %(pathname)s[:%(lineno)s] %(name)s\n%(absolute_path)s\n%(topline)s\n%(traceback)s\n\n\n[%(duration).3f]\n%(statement)s\n%(botline)s\n',
            #'format': '%(topline)s\n%(asctime)s:::::::::SQL:::::::::::%(levelname)-1s\n%(botline)s\n%(traceback)s\n\n\n[%(duration).3f]\n%(statement)s\n%(botline)s\n',
        },
        'verbose2': {
            '()': VerFormatter2,
            'format': '%(topline)s\n%(asctime)s--XXX%(levelname)sXXX %(funcName)s() %(pathname)s[:%(lineno)s] %(name)s\n%(absolute_path)s\n%(botline)s\n%(message)s\n%(botline)s\n',
            #'datefmt': "[%d/%b/%Y %H:%M:%S %p %Z]"
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'formatter': 'verbose',
            'class': 'logging.StreamHandler',
        },
        'console2': {
            'level': 'DEBUG',
            'formatter': 'verbose2',
            'class': 'logging.StreamHandler',
        },
        'sql': {
            'class': 'logging.StreamHandler',
            'formatter': 'sql',
            'level': 'DEBUG',
        },
    },
    'filters': {
        'myfilter': {
            '()': LoggerGate,
        }
    },
    'loggers': {
        'custom_string': {
            'level': 'DEBUG' if DEBUG else 'INFO',
            'handlers': ['console'],
            'propagate': False,
        },
        # added from django-request-logging
        'django.request': {
            'handlers': ['console2'],
            'level': logging.CRITICAL if DEBUG else 'INFO',  # change debug level as appropiate
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['sql'],
            'level': 'DEBUG',
            'propagate': False,
            'filters': ['myfilter']
        },
    },
}

# added from django-LoggingMiddleware
REQUEST_LOGGING_DATA_LOG_LEVEL=logging.CRITICAL
REQUEST_LOGGING_HTTP_4XX_LOG_LEVEL=logging.CRITICAL
REQUEST_LOGGING_MAX_BODY_LENGTH = 1000000000



#############################


# for django ORM to work in jupyter
# https://stackoverflow.com/a/62119475
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"




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
def pp_odir(obj):

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
