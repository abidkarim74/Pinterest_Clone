# Generated by Django 5.1.5 on 2025-01-21 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0008_remove_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='postImages/'),
        ),
    ]
