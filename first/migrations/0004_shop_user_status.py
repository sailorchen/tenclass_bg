# Generated by Django 3.1.4 on 2021-07-29 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0003_auto_20210729_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop_user',
            name='status',
            field=models.IntegerField(default=1, verbose_name='状态:1正常 0不正常'),
        ),
    ]
