# Generated by Django 5.0.6 on 2024-06-15 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("school", "0003_remove_student_teacher_student_teachers"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="teachers",
            field=models.ManyToManyField(
                related_name="students", to="school.teacher", verbose_name="Учителя"
            ),
        ),
    ]
