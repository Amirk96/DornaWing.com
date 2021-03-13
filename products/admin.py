from django.contrib import admin
from wagtail.contrib.modeladmin.options import (
	ModelAdmin,
	modeladmin_register,

	)
from .models import PostsModel


class PostsAdmin(ModelAdmin):
	model = PostsModel
	menu_label = "PRODUCTS"
	menu_icon = "tick-inverse"
	menu_order = 291
	add_to_settings_menu = False
	exclude_from_explorer = False
	list_display = ("products_title",
					"updated_time",
					"created_time",
					"pub_time",
		)

modeladmin_register(PostsAdmin)
