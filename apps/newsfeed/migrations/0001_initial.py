# Generated by Django 3.2.6 on 2021-08-18 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.TextField(blank=True, null=True, unique=True)),
                ('thumbnail', models.URLField(blank=True, null=True)),
                ('source', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('published_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
