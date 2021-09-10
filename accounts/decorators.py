from django.http import HttpResponse
from django.shortcuts import redirect

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                print(group)
            if group in allowed_roles:
                print('exists')
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('<center><h1>You are not authorized to view this page')

        return wrapper_func
    return decorator

