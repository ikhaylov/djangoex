# Generated by Django 3.1.2 on 2020-10-30 11:24

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20201023_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='RichTextField'),
        ),
    ]