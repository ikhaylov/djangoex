# Generated by Django 3.1.2 on 2020-10-21 05:35

from django.db import migrations
import django.utils.timezone
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20201016_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='text',
            field=django_ckeditor_5.fields.CKEditor5Field(default=django.utils.timezone.now, verbose_name='CKEditor5Field'),
            preserve_default=False,
        ),
    ]