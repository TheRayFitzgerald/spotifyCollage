# Generated by Django 4.1.1 on 2022-09-26 07:46

from django.db import migrations



from django.db import migrations

def create_data(apps, schema_editor):
    Album = apps.get_model('display_collage', 'Album')
    Album(title="Album title", cover_art_url="google.com    ").save()

class Migration(migrations.Migration):

    dependencies = [
        ('display_collage', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]