#from django.conf import settings
from a2infinity.external_config import api_local_settings

def RequestExposerMiddleware(get_response):
    def middleware(request):
        import datetime
        url = request.build_absolute_uri()
        method = request.method
        current_time = datetime.datetime.utcnow()
        tag = f"{current_time}_{method}_{url}"

        print(f"<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<{tag}")
        api_local_settings.exposed_request.append(tag)

        response = get_response(request)

        api_local_settings.exposed_request.remove(tag)
        print(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>{tag}")

        return response

    return middleware