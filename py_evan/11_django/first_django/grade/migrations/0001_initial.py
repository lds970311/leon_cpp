# Generated by Django 4.2.2 on 2023-06-23 13:55

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=32, verbose_name='学生的姓名')),
                ('subject_name', models.CharField(max_length=32, verbose_name='科目')),
                ('score', models.FloatField(default=0, verbose_name='分数')),
                ('year', models.SmallIntegerField(verbose_name='年份')),
            ],
            options={
                'db_table': 'grade',
            },
        ),
    ]
