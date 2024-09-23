from .models import CustomUser

def deleteMember(request, user):
    if request.user.is_superuser:
        CustomUser.objects.filter(member_no=user).delete()
        return True
    else:
        return False

def updateMember(request):
    pass
