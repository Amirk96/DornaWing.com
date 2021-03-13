from django.contrib import admin
from wagtail.contrib.modeladmin.options import (
	ModelAdmin,
	modeladmin_register,

	)
from .models import PostsModel


class PostsAdmin(ModelAdmin):
	model = PostsModel
	menu_label = "NEWS"
	menu_icon = "site"
	menu_order = 290
	add_to_settings_menu = False
	exclude_from_explorer = False
	list_display = ("news_title",
					"updated_time",
					"created_time",
					"pub_time",
		)

modeladmin_register(PostsAdmin)
