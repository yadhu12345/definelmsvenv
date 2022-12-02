# Generated by Django 4.1.1 on 2022-12-02 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lmsmainapp', '0017_video_class_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(default='', max_length=5000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmsmainapp.login')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmsmainapp.video_class')),
            ],
            options={
                'db_table': 'comment',
            },
        ),
    ]