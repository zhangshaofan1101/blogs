from django.db import models

# Create your models here.

class Catagory(models.Model):
    """
    博客分类
    """
    name = models.CharField('名称', max_length=30)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    """
    博客标签
    """
    name = models.CharField('名称', max_length=16)

    def __unicode__(self):
        return self.name


class Blog(models.Model):
    """
    博客
    """
    title = models.CharField('标题', max_length=32)
    author = models.CharField('作者', max_length=16)
    content = models.TextField('博客正文')
    created = models.DateTimeField('发布时间', auto_now_add=True)
    catagory = models.ForeignKey(Catagory, verbose_name='分类',on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name='标签')

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    """
    评论
    """
    blog = models.ForeignKey(Blog, verbose_name='博客',on_delete=models.DO_NOTHING)
    name = models.CharField('称呼', max_length=16)
    email = models.EmailField('邮箱')
    content = models.CharField('内容', max_length=240)
    created = models.DateTimeField('发布时间', auto_now_add=True)

    def __unicode__(self):
        return self.content