from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from django.contrib import messages

class CheckSuperuserMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        # Check if the user is not a superuser and accessing a restricted view
        if not request.user.is_superuser:
            messages.error(request, "You do not have permission to access this page login as admin.")
            return redirect('/')
        return None
