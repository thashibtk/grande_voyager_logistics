from django.contrib import admin
from .models import *
from unfold.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.admin import register
from django.contrib.auth.models import User
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm

admin.site.unregister(User)

@register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

class BlogAdmin(ModelAdmin):
    list_display = ('blog_title', 'posted_on')
admin.site.register(Blog, BlogAdmin)

class ContactAdmin(ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ['name', 'email', 'phone']
admin.site.register(Contact, ContactAdmin)

class NewsletterAdmin(ModelAdmin):
    pass
admin.site.register(Newsletter, NewsletterAdmin)

class ServicesAdmin(ModelAdmin):
    search_fields = ['service_title',]
    list_display = ('service_title', 'priority',)
admin.site.register(Services, ServicesAdmin)

class CertificatesAdmin(ModelAdmin):
    pass
admin.site.register(Certificates, CertificatesAdmin)