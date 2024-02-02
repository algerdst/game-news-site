# Generated by Django 4.1.7 on 2023-03-28 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="article",
            options={"verbose_name": "Статья", "verbose_name_plural": "Статьи"},
        ),
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Категория", "verbose_name_plural": "Категории"},
        ),
        migrations.AlterField(
            model_name="article",
            name="image",
            field=models.ImageField(
                default="images/default.jpg", upload_to="media/media/images"
            ),
        ),
    ]
