# Generated by Django 4.1.1 on 2022-10-05 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display_collage', '0003_remove_album_id_alter_album_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='cover_art_img',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]