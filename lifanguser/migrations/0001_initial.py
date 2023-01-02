# Generated by Django 4.1.3 on 2022-12-06 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Lifanguser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=128, verbose_name="사용자 이메일")),
                ("password", models.CharField(max_length=64, verbose_name="비밀번호")),
                (
                    "registered_dttm",
                    models.DateTimeField(auto_now_add=True, verbose_name="등록시간"),
                ),
            ],
            options={
                "verbose_name": "사용자",
                "verbose_name_plural": "사용자",
                "db_table": "lifang_django_lifanguser",
            },
        ),
    ]