# Generated by Django 3.1.4 on 2021-01-05 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rec', '0004_auto_20210104_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='Subj',
            field=models.CharField(choices=[('Python', 'Python'), ('JQUERY', 'jQuery'), ('JavaScript', 'JavaScript')], default='Python', max_length=10),
        ),
    ]