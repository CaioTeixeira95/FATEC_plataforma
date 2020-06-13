# Generated by Django 2.2.13 on 2020-06-09 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Usuário', 'verbose_name_plural': 'Usuários'},
        ),
        migrations.AlterField(
            model_name='user',
            name='is_company',
            field=models.BooleanField(default=False, verbose_name='Empresa'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_student',
            field=models.BooleanField(default=False, verbose_name='Estudante'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_teacher',
            field=models.BooleanField(default=False, verbose_name='Professor'),
        ),
    ]