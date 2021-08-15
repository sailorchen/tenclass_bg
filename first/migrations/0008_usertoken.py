# Generated by Django 3.1.4 on 2021-08-15 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0007_auto_20210731_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usertoken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=512)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='first.shop_user')),
            ],
            options={
                'verbose_name': '授权表',
                'verbose_name_plural': '授权表',
            },
        ),
    ]
