# Generated by Django 5.1.2 on 2024-10-19 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.AddField(
            model_name='products',
            name='sales_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='products',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]