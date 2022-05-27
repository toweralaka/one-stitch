from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin as CoreFlatPageAdmin
from django.contrib.flatpages.forms import FlatpageForm as CoreFlatpageForm
from django.utils.translation import gettext_lazy as _

from .models import MainSite, UserProfile
# Register your models here.


class MainSiteForm(CoreFlatpageForm):
    class Meta:
        model = MainSite
        fields = '__all__'


class MainSiteAdmin(CoreFlatPageAdmin):
    form = MainSiteForm
    fieldsets = (
        (None, {'fields': (
            'url', 'title', 'name', 'head_office', 'logo', 'favicon', 'introduction',
            'school_main_color', 'school_secondary_color', 'phone', 'email', 'website',
            'facebook', 'twitter', 'instagram', 'youtube', 'whatsapp', 'social_image',
            'sites')}),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': (
                'enable_comments',
                'registration_required',
                'template_name',
            ),
        }),
    )



admin.site.register(MainSite, MainSiteAdmin)
admin.site.register(UserProfile)
admin.site.site_header = 'One Stitch Administration'
admin.site.site_title = 'One Stitch Admin'
# admin.site.site_url = 'user'
admin.site.index_title = 'Admin Dashboard'
# admin.site.app_index_template = 'index.html'
