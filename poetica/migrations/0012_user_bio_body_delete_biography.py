# Generated by Django 4.0.2 on 2022-05-09 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poetica', '0011_biography'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio_body',
            field=models.TextField(blank=True, max_length=256, null=True),
        ),
        migrations.DeleteModel(
            name='Biography',
        ),
    ]
