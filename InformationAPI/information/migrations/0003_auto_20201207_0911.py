# Generated by Django 3.1.4 on 2020-12-07 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0002_subcategory_subcat_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='category',
            new_name='user_category',
        ),
    ]
