# Generated by Django 3.1.2 on 2020-10-10 19:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0002_remove_userinformation_aliasname'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinformation',
            options={'ordering': ['-date_joined'], 'verbose_name': '用户信息', 'verbose_name_plural': '用户信息'},
        ),
        migrations.CreateModel(
            name='ConfirmString',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=256)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '确认码',
                'verbose_name_plural': '确认码',
                'ordering': ['-create_time'],
            },
        ),
    ]
