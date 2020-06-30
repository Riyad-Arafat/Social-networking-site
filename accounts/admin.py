from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile, Users

# Register your models here.





class AccountAdmin(UserAdmin):
	list_display = ('email','username','date_joined', 'last_login', 'is_admin','is_staff',)
	search_fields = ('email','username',)
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ('is_admin','is_staff','last_login')
	fieldsets = ()


admin.site.register(Users, AccountAdmin)

admin.site.register(Profile)