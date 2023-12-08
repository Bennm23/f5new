# f5members/decorators.py
from functools import wraps
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

def is_in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

def group_access_only(group_name, view_to_return="members:error", message="Access denied."):
    def decorator(view):
        @wraps(view)
        def _wrapped_view(request, *args, **kwargs):
            if not is_in_group(request.user, group_name):
                messages.error(request, message)
                return redirect(view_to_return)
            return view(request, *args, **kwargs)
        return _wrapped_view
    return decorator
