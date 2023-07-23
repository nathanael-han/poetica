# Generated by Django 4.0.2 on 2022-05-09 03:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poetica', '0013_remove_user_bio_body_biography'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_body', models.TextField(max_length=256)),
                ('poet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_status', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Biography',
        ),
    ]
