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


class NewsPage(Page):
	max_count = 1

	def get_context(self, request):
		context = super().get_context(request)
		context['posts'] = PostsModel.objects.all()
		context['social'] = SocialMediaModel.objects.all()       
		return context


class PostsModel(models.Model):
	news_title = models.CharField('News Title', max_length=50, default=" ")
	news_text = RichTextField('News Text', max_length=1000, default=" ")
	news_img = models.ForeignKey(
		"wagtailimages.Image",
		blank=False,
		null=True,
		related_name="+",
		on_delete=models.SET_NULL,
		)

	updated_time = models.DateTimeField('updated_time', auto_now=True)
	created_time = models.DateTimeField('created_time', auto_now_add=True)
	pub_time = models.DateTimeField('pub_time', auto_now_add=True)

	def __str__(self):
		return "{} - {}".format(self.news_title, self.pub_time)

	panels = [
		FieldPanel('news_title'),
		FieldPanel('news_text'),
		ImageChooserPanel('news_img')
	]

	class Meta:
		ordering = ['pub_time']
		verbose_name_plural = "News"
