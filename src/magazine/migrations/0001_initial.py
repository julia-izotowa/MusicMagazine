# Generated by Django 3.2.13 on 2022-06-29 17:51

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("uuid", models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)),
                ("cover_image", models.ImageField(default="", upload_to="media/covers")),
                ("title", models.CharField(max_length=1024)),
                ("text", models.TextField()),
                ("publication_date", models.DateTimeField(auto_now_add=True)),
                ("edit_date", models.DateTimeField(auto_now=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="articles",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="ArticleTag",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="article_tags", to="magazine.article"
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="article_tags", to="magazine.tag"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="article",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="articles", to="magazine.category"
            ),
        ),
    ]
