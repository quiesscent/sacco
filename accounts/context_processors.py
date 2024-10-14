from .models import CustomUser

def profile_image(request):
    profile = None

    if request.user.is_authenticated:
        user_profile = CustomUser.objects.filter(email=request.user).first()
        if user_profile:
            profile = user_profile.profile

    return {'profile': profile}
