# Generated by Django 3.1.1 on 2020-09-19 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth0authorization', '0002_image_thought'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='twitterId',
            field=models.TextField(blank=True, null=True),
        ),
    ]
