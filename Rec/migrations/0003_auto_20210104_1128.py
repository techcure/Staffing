# Generated by Django 3.1.4 on 2021-01-04 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rec', '0002_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='headline',
            new_name='Que',
        ),
        migrations.AddField(
            model_name='question',
            name='Ans',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
