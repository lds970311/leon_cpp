from django.db import models


class Grade(models.Model):
    """ 学生成绩 """
    student_name = models.CharField('学生的姓名', max_length=32)
    subject_name = models.CharField('科目', max_length=32)
    score = models.FloatField('分数', default=0)
    year = models.SmallIntegerField('年份')

    class Meta:
        db_table = 'grade'
