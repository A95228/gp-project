from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User
admin.register(User)
# class UserAdmin(BaseUserAdmin):
#     # The forms to add and change user instances
#     form = UserAdminChangeForm
#     add_form = UserAdminCreationForm

#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
#     list_display = ('email', 'admin')
#     list_filter = ('admin',)
#     fieldsets = (
#         (None, {'fields': ('username', 'email', 'password')}),
#         ('Personal info', {'fields': ()}),
#         ('Permissions', {'fields': ('admin',)}),
#     )
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2')}
#         ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)
#     filter_horizontal = ()


# admin.site.register(User, UserAdmin)



# Remove Group Model from admin. We're not using it.
# admin.site.unregister(Group)
# from .models import User

# class UserAdmin(admin.ModelAdmin):
#     fields = ['email', 'username', 'full_name', 'password', 'is_active', 'staff', 'admin', 'is_confirm']
# # Register your models here.
# admin.site.register(User, UserAdmin)

# , 'email', 'full_name', 'password', 'is_active', 'is_staff', 'is_admin'