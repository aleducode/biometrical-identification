# Generated by Django 2.2 on 2019-05-02 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20190502_0226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dactilaridentification',
            name='created',
        ),
        migrations.RemoveField(
            model_name='dactilaridentification',
            name='modified',
        ),
    ]
