# Generated by Django 5.0.6 on 2024-06-15 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tag",
            options={
                "ordering": ["name"],
                "verbose_name": "Тэг",
                "verbose_name_plural": "Тэги",
            },
        ),
        migrations.RenameField(
            model_name="article",
            old_name="theme",
            new_name="tags",
        ),
        migrations.RenameField(
            model_name="scope",
            old_name="theme",
            new_name="tag",
        ),
    ]
