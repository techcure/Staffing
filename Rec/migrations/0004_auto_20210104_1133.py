# Generated by Django 3.1.4 on 2021-01-04 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rec', '0003_auto_20210104_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='Ans',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
