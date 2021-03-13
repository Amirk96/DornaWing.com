# Generated by Django 3.1.6 on 2021-02-13 19:10

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('wagtailimages', '0022_uploadedimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='PostsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products_title', models.CharField(default=' ', max_length=50, verbose_name='Products Title')),
                ('products_text', wagtail.core.fields.RichTextField(default=' ', max_length=500, verbose_name='Products Text')),
                ('left_table', wagtail.core.fields.StreamField([('Left_Table', wagtail.core.blocks.CharBlock(form_classname='full title'))])),
                ('right_table', wagtail.core.fields.StreamField([('Right_Table', wagtail.core.blocks.CharBlock(form_classname='full title'))])),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('pub_time', models.DateTimeField(auto_now_add=True, verbose_name='Published Time')),
                ('products_img', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ['pub_time'],
            },
        ),
    ]
