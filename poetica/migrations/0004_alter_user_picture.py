# Generated by Django 4.0.2 on 2022-05-01 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poetica', '0003_user_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.URLField(blank=True, default='poetica/assets/default.png', null=True),
        ),
    ]
