# Generated by Django 5.0.4 on 2024-04-21 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0004_alter_anonymousshortify_url_delete_shortify'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anonymousshortify',
            options={'ordering': ['-id']},
        ),
    ]
