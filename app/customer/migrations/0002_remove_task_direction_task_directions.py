# Generated by Django 4.2.5 on 2024-04-21 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelancer', '0004_freelancer_contact_info_alter_freelancer_description_and_more'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='direction',
        ),
        migrations.AddField(
            model_name='task',
            name='directions',
            field=models.ManyToManyField(blank=True, null=True, to='freelancer.direction', verbose_name='Направления'),
        ),
    ]