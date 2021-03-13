from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from django.contrib.auth.models import User
from wagtail.documents.models import Document
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
	FieldPanel, FieldRowPanel,
	InlinePanel, MultiFieldPanel
)
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField, AbstractForm
from django.forms import widgets  # used to find TextArea widget


class SingletonModel(models.Model):

	class Meta:
		abstract = True

	def save(self, *args, **kwargs):
		self.pk = 1
		super(SingletonModel, self).save(*args, **kwargs)

	def delete(self, *args, **kwargs):
		pass

	@classmethod
	def load(cls):
		obj, created = cls.objects.get_or_create(pk=1)
		return obj


class SocialMediaModel(SingletonModel):
	twitter = models.URLField(verbose_name='Twitter Web Page (Company)', null=True, blank=True, unique=True)
	facebook = models.URLField(verbose_name='Facebook Web Page (Company)', null=True, blank=True, unique=True)
	instagram = models.URLField(verbose_name='Email Address (Company)', null=True, blank=True, unique=True)
	linkedin = models.URLField(verbose_name='Linedin Web Page (Company)', null=True, blank=True, unique=True)


class FormField(AbstractFormField):
	page = ParentalKey('HomePage', on_delete=models.CASCADE, related_name='form_fields')


class HomePage(AbstractEmailForm, Page):  
	
	def get_form(self, *args, **kwargs):
		form = super().get_form(*args, **kwargs)
		# iterate through the fields in the generated form
		for name, field in form.fields.items():
			# here we want to adjust the widgets on each field
			# if the field is a TextArea - adjust the rows
			if isinstance(field.widget, widgets.Textarea):
				field.widget.attrs.update({'rows': '6'})
				placeholder = name.replace("_", " ")
				field.widget.attrs.update({'placeholder': placeholder.capitalize()})
				# for all fields, get any existing CSS classes and add 'form-control'
				# ensure the 'class' attribute is a string of classes with spaces
				css_classes = field.widget.attrs.get('class', '').split()
				css_classes.append('form-control')
				field.widget.attrs.update({'class': ' '.join(css_classes)})

			if isinstance(field.widget, widgets.Input):
				field.widget.attrs.update({'rows': '6'})
				placeholder = name.replace("_", " ")
				field.widget.attrs.update({'placeholder': placeholder.capitalize()})
				# for all fields, get any existing CSS classes and add 'form-control'
				# ensure the 'class' attribute is a string of classes with spaces
				css_classes = field.widget.attrs.get('class', '').split()
				css_classes.append('form-control')
				field.widget.attrs.update({'class': ' '.join(css_classes)})
		return form

	template = "home/home_page.html"
	# This is the default path.
	# If ignored, Wagtail adds _landing.html to your template name
	landing_page_template = "home/landing_home_page.html"
	banner_image = models.ForeignKey(
		"wagtailimages.Image",
		blank=False,
		null=True,
		related_name="+",
		on_delete=models.SET_NULL,
		)
	header_title_text = models.CharField('Header Title', max_length=50, default=" ")
	header_text = models.CharField('Header Text', max_length=100, default=" ")

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
	
	location = models.CharField('Location', max_length=50, default=" ")
	email = models.CharField('Email', max_length=50, default=" ")
	call = models.CharField('Call', max_length=50, default=" ") 
	  

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

	FieldPanel('location', classname="full"),
	FieldPanel('email', classname="full"),
	FieldPanel('call', classname="full"),

	InlinePanel('form_fields', label="Form fields"),    
	]

	def get_context(self, request):
		context = super().get_context(request) 
		context['social'] = SocialMediaModel.objects.all()       
		return context