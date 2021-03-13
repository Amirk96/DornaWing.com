from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from django.contrib.auth.models import User
from wagtail.documents.models import Document
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList
from home.models import SocialMediaModel


class ProductsPage(Page):
	max_count = 1

	def get_context(self, request):
		context = super().get_context(request)
		context['posts'] = PostsModel.objects.all()
		context['social'] = SocialMediaModel.objects.all()
		return context

class PostsModel(models.Model):
	products_title = models.CharField('Products Title', max_length=50, default=" ")
	products_text = RichTextField('Products Text', max_length=1000, default=" ")
	products_img = models.ForeignKey(
		"wagtailimages.Image",
		blank=False,
		null=True,
		related_name="+",
		on_delete=models.SET_NULL,
		)
	left_table = StreamField([
		('Left_Table', blocks.CharBlock(form_classname="full title")),
	])
	right_table = StreamField([
		('Right_Table', blocks.CharBlock(form_classname="full title")),
	])

	updated_time = models.DateTimeField('Updated Time', auto_now=True)
	created_time = models.DateTimeField('Created Time', auto_now_add=True)
	pub_time = models.DateTimeField('Published Time', auto_now_add=True)

	def __str__(self):
		return "{} - {}".format(self.products_title, self.pub_time)

	class Meta:
		ordering = ['pub_time']
		verbose_name_plural = "Products"

	panels = [
		FieldPanel('products_title'),
		FieldPanel('products_text'),
		ImageChooserPanel('products_img'),
		StreamFieldPanel('left_table'),
		StreamFieldPanel('right_table')
	]
	
	def get_context(self, request):
		context = super().get_context(request)
		return context
