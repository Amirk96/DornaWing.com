from django.contrib import admin
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,

)
from .models import SocialMediaModel


class SocialMediaAdmin(ModelAdmin):
    model = SocialMediaModel
    menu_label = "Social network"
    menu_icon = "site"
    menu_order = 293
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("twitter",
                    "facebook",
                    "instagram",
                    "linkedin",
    )

modeladmin_register(SocialMediaAdmin)