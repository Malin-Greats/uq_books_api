# Generated by Django 4.0.4 on 2022-05-12 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0002_bookreview_is_approved_bookreview_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookpublish',
            name='description',
            field=models.TextField(blank=True, default='test description is here', max_length=1000, null=True),
        ),
    ]
