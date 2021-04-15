# Generated by Django 2.2 on 2021-04-11 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_follow_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, help_text='Введите название группы', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='api.Group', verbose_name='Группа'),
        ),
    ]
