# Generated by Django 4.1.1 on 2022-11-04 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsmainapp', '0012_delete_designation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question_bank',
            name='question',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
