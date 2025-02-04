# Generated by Django 4.0.5 on 2022-07-04 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0002_alter_author_options_alter_book_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(max_length=20000, verbose_name='Atsiliepimas')),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='library.book', verbose_name='knyga')),
                ('reviewer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to=settings.AUTH_USER_MODEL, verbose_name='skaitytojas')),
            ],
        ),
    ]
