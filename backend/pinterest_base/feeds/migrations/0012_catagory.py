# Generated by Django 5.1.5 on 2025-01-26 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0011_alter_post_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
