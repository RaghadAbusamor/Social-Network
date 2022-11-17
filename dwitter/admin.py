from django.contrib import admin

# dwitter/admin.py
from django.contrib import admin
from django.contrib.auth.models import Group
admin.site.unregister(Group)
# Register your models here.


# Only display the "username" field
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
