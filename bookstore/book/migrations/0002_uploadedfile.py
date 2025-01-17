# Generated by Django 5.1.4 on 2025-01-03 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('visibility', models.BooleanField(default=True)),
                ('cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('year_published', models.IntegerField(blank=True, null=True)),
                ('file', models.FileField(upload_to='uploads/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
