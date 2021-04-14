from django.contrib.sessions.models import Session
from django.contrib import messages
from django.shortcuts import redirect


class SingleSessionPerUser:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        if request.user.is_authenticated:
            active_session_key = request.user.logged_in_user.session_key

            if active_session_key and active_session_key != request.session.session_key:
                Session.objects.get(session_key=active_session_key).delete()

            request.user.logged_in_user.session_key = request.session.session_key
            request.user.logged_in_user.save()


        response = self.get_response(request)

     
        return response



