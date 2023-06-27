from django.db.models import Sum
from django.shortcuts import render

from .models import Grade


def page_grade(request):
    """ 学生成绩的统计 """
    grade_list = Grade.objects.filter(student_name='张三')
    total = grade_list.aggregate(Sum('score'))
    print(total)
    return render(request, 'page_grade.html', {
        'total': total
    })
