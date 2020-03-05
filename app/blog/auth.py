from django.shortcuts import get_object_or_404
from .models import User

def custom_authenticate(request):
    user_id = request.POST['user_id']
    password = request.POST['password']

    try:
        user = get_object_or_404(User, user_id=user_id, password=password)
        if user is not None:
            return user
    except:
        return None
    return None
