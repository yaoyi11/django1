from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(verbose_name='电影名称', max_length=30)
    movie_cate = models.CharField(verbose_name='电影分类', max_length=30, blank=True, null=True)
    movie_img = models.CharField(verbose_name='封面图片', max_length=300, null=True, blank=True)
    release_date = models.DateField(verbose_name='上映日期')
    viewed = models.BooleanField(verbose_name='观看状态', default=False)
    created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '电影'
        verbose_name_plural = verbose_name
        ordering = ('name',)