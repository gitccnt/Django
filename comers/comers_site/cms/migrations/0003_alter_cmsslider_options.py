# Generated by Django 4.1.3 on 2022-11-28 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_cmsslider_cms_css'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cmsslider',
            options={'verbose_name': 'Slide', 'verbose_name_plural': 'Slides'},
        ),
    ]