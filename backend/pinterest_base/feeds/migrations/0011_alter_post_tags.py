# Generated by Django 5.1.5 on 2025-01-26 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0010_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts', to='feeds.tag'),
        ),
    ]
