# Generated by Django 4.1.1 on 2022-10-25 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('display_collage', '0002_collage_img_str'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collage',
            name='img',
        ),
    ]
