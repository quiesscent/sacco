from django.contrib import admin
from .models import CustomUser, MemberDependent, MemberProfile, Notification, Contributions, OverallContribution
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ('wide',),
                "fields": ("username", "email", "id_number","member_no", "password1", "password2", "profile"),
            },
        ),
    )
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(MemberDependent)
admin.site.register(MemberProfile)
admin.site.register(Notification)
admin.site.register(Contributions)
admin.site.register(OverallContribution)
