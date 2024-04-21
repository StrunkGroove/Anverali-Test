# Generated by Django 4.2.5 on 2024-04-21 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelancer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelancer',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='freelancer',
            name='direction',
            field=models.CharField(blank=True, choices=[('web', 'Веб-разработка'), ('mobile', 'Мобильная разработка'), ('design', 'Дизайн'), ('translater', 'Переводчик')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='freelancer',
            name='experience',
            field=models.IntegerField(blank=True, choices=[(1, 'Менее 1 года'), (2, '1-3 года'), (3, '3-5 лет'), (4, 'Более 5 лет')], null=True),
        ),
    ]
