from .models import MemberProfile

def profile_image(request):
    profile_picture = None

    if request.user.is_authenticated:
        user_profile = MemberProfile.objects.filter(user=request.user).first()
        if user_profile:
            profile_picture = user_profile.profile_picture

    return {'profile_picture': profile_picture}