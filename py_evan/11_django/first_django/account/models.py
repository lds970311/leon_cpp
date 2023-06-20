from django.db import models


class CommonModel(models.Model):
    """
    自定义模型的基类
    """
    create_time = models.DateTimeField('注册时间', auto_now_add=True)
    update_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        abstract = True


class User(CommonModel):
    name = models.CharField('姓名', max_length=64)
    sex = models.CharField('性别', max_length=1, choices=(
        ('1', '男'),
        ('2', '女')
    ), default='1')
    age = models.PositiveIntegerField('年龄', default=0)
    username = models.CharField('用户名', max_length=255, unique=True)
    password = models.CharField('密码', max_length=128, unique=True)
    remark = models.CharField('备注', max_length=256, null=True, blank=True)

    collect_ques = models.ManyToManyField('Question')

    class Meta:
        db_table = 'user'


class Profile(CommonModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    nickname = models.CharField('昵称', max_length=64)


class Question(CommonModel):
    name = models.CharField('问题名称', max_length=64)


class Answer(CommonModel):
    qustion = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer',
                                verbose_name='关联的问题')
    content = models.TextField('答案内容')


class Classify(models.Model):
    """ 分类
    1 酒水
       2 啤酒
       3 白酒
    """
    name = models.CharField('名称', max_length=64)
    parent = models.ForeignKey('self', related_name='children',
                               on_delete=models.CASCADE)
