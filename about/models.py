from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from django.contrib.auth.models import User
from wagtail.documents.models import Document
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList
from home.models import SocialMediaModel
from wagtail.admin.edit_handlers import (
	FieldPanel, FieldRowPanel,
	InlinePanel, MultiFieldPanel
)
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField, AbstractForm
from django.forms import widgets  # used to find TextArea widget

class AboutPage(Page):
	banner_image = models.ForeignKey(
		"wagtailimages.Image",
		blank=False,
		null=True,
		related_name="+",
		on_delete=models.SET_NULL,
		)
	header_title_text = models.CharField('Header Title', max_length=100, default=" ")
	header_text = models.CharField('Header Text', max_length=200, default=" ")

	about_title = models.CharField('About Title', max_length=100, default=" ")
	about_left_richtext = RichTextField('About Us Left Paragraph', max_length=500, blank=True)
	about_right_richtext = RichTextField('About Us Right Paragraph', max_length=500, blank=True)
	about_us_img = models.ForeignKey(
		"wagtailimages.Image",
		blank=False,
		null=True,
		related_name="+",
		on_delete=models.SET_NULL,
		)
	

	first_member_of_team_img = models.ForeignKey(
		"wagtailimages.Image",
		blank=False,
		null=True,
		related_name="+",
		on_delete=models.SET_NULL,
		)
	first_member_of_team_twitter = models.URLField(verbose_name='Twitter web page', null=True, blank=True, unique=True)
	first_member_of_team_facebook = models.URLField(verbose_name='Facebook web page', null=True, blank=True, unique=True)
	first_member_of_team_instagram = models.URLField(verbose_name='Email Address', null=True, blank=True, unique=True)
	first_member_of_team_linkedin = models.URLField(verbose_name='Linedin web page', null=True, blank=True, unique=True)
	first_member_of_team_name = models.CharField('Full Name', max_length=30, default=" ")
	first_member_of_team_position = models.CharField('Organizational Position', max_length=30, default=" ")
	first_member_of_team_description = models.CharField('Description', max_length=100, default=" ")


	second_member_of_team_img = models.ForeignKey(
		"wagtailimages.Image",
		blank=False,
		null=True,
		related_name="+",
		on_delete=models.SET_NULL,
		)
	second_member_of_team_twitter = models.URLField(verbose_name='Twitter web page', null=True, blank=True, unique=True)
	second_member_of_team_facebook = models.URLField(verbose_name='Facebook web page', null=True, blank=True, unique=True)
	second_member_of_team_instagram = models.URLField(verbose_name='Email Address', null=True, blank=True, unique=True)
	second_member_of_team_linkedin = models.URLField(verbose_name='Linedin web page', null=True, blank=True, unique=True)
	second_member_of_team_name = models.CharField('Full Name', max_length=30, default=" ")
	second_member_of_team_position = models.CharField('Organizational Position', max_length=30, default=" ")
	second_member_of_team_description = models.CharField('Description', max_length=100, default=" ")

	third_member_of_team_img = models.ForeignKey(
		"wagtailimages.Image",
		blank=False,
		null=True,
		related_name="+",
		on_delete=models.SET_NULL,
		)
	third_member_of_team_twitter = models.URLField(verbose_name='Twitter web page', null=True, blank=True, unique=True)
	third_member_of_team_facebook = models.URLField(verbose_name='Facebook web page', null=True, blank=True, unique=True)
	third_member_of_team_instagram = models.URLField(verbose_name='Email Address', null=True, blank=True, unique=True)
	third_member_of_team_linkedin = models.URLField(verbose_name='Linedin web page', null=True, blank=True, unique=True)
	third_member_of_team_name = models.CharField('Full Name', max_length=30, default=" ")
	third_member_of_team_position = models.CharField('Organizational Position', max_length=30, default=" ")
	third_member_of_team_description = models.CharField('Description', max_length=100, default=" ")
	
	updated_time = models.DateTimeField('updated_time', auto_now=True)
	created_time = models.DateTimeField('created_time', auto_now_add=True)
	pub_time = models.DateTimeField('pub_time', auto_now_add=True)

	max_count = 1

	content_panels = Page.content_panels + [
	ImageChooserPanel('banner_image'),
	FieldPanel('header_title_text', classname="full"),
	FieldPanel('header_text', classname="full"),

	FieldPanel('about_title', classname="full"),
	FieldPanel('about_left_richtext', classname="full"),
	FieldPanel('about_right_richtext', classname="full"),
	ImageChooserPanel('about_us_img'),

	ImageChooserPanel('first_member_of_team_img'),
	FieldPanel('first_member_of_team_twitter', classname="full"),
	FieldPanel('first_member_of_team_facebook', classname="full"),
	FieldPanel('first_member_of_team_instagram', classname="full"),
	FieldPanel('first_member_of_team_linkedin', classname="full"),
	FieldPanel('first_member_of_team_name', classname="full"),
	FieldPanel('first_member_of_team_position', classname="full"),
	FieldPanel('first_member_of_team_description', classname="full"),


	ImageChooserPanel('second_member_of_team_img'),
	FieldPanel('second_member_of_team_twitter', classname="full"),
	FieldPanel('second_member_of_team_facebook', classname="full"),
	FieldPanel('second_member_of_team_instagram', classname="full"),
	FieldPanel('second_member_of_team_linkedin', classname="full"),
	FieldPanel('second_member_of_team_name', classname="full"),
	FieldPanel('second_member_of_team_position', classname="full"),
	FieldPanel('second_member_of_team_description', classname="full"),


	ImageChooserPanel('third_member_of_team_img'),
	FieldPanel('third_member_of_team_twitter', classname="full"),
	FieldPanel('third_member_of_team_facebook', classname="full"),
	FieldPanel('third_member_of_team_instagram', classname="full"),
	FieldPanel('third_member_of_team_linkedin', classname="full"),
	FieldPanel('third_member_of_team_name', classname="full"),
	FieldPanel('third_member_of_team_position', classname="full"),
	FieldPanel('third_member_of_team_description', classname="full"),
	]

	def get_context(self, request):
		context = super().get_context(request)
		context['social'] = SocialMediaModel.objects.all()             
		return context