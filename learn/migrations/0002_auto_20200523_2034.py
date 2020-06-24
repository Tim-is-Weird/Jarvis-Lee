# Generated by Django 3.0.6 on 2020-05-23 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='choice_a',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='choice_b',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='choice_c',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='choice_d',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='test_number',
            field=models.CharField(max_length=25, null=True),
        ),
    ]