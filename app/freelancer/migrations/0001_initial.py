# Generated by Django 4.2.5 on 2024-04-21 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Freelancer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.IntegerField(choices=[(1, 'Менее 1 года'), (2, '1-3 года'), (3, '3-5 лет'), (4, 'Более 5 лет')])),
                ('description', models.TextField()),
                ('direction', models.CharField(choices=[('web', 'Веб-разработка'), ('mobile', 'Мобильная разработка'), ('design', 'Дизайн'), ('translater', 'Переводчик')], max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='freelancer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
