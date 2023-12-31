# Generated by Django 4.2.2 on 2023-06-23 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StoredEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=64)),
                ('message', models.TextField()),
                ('from_email', models.EmailField(max_length=254)),
                ('to_email', models.EmailField(max_length=254)),
                ('cc_email', models.TextField(blank=True)),
                ('attachment', models.FileField(blank=True, upload_to='attachments/')),
                ('sent_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
