from time import strftime

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

#
# class Registration(models.Model):
#     username = models.CharField(max_length=100)


class BlogModel(models.Model):
    title = models.CharField(max_length=150, blank=False)
    description = models.TextField(max_length=5000, blank=False)

    def __str__(self):
        return self.title


class DocxModel(models.Model):
    title = models.CharField(max_length=500, name='title')
    docx = models.FileField(upload_to='files')

    def __str__(self):
        return self.title


class CatModel(models.Model):
    status = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.status


class FAQModel(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField(max_length=1000)

    def __str__(self):
        return '%s  : %s' % (self.question, self.answer)


class ListModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='User', on_delete=models.CASCADE)
    topic = models.ForeignKey(DocxModel, on_delete=models.CASCADE, related_name='topic')
    status = models.ForeignKey(CatModel, on_delete=models.CASCADE, default="TO DO", name='status')
    endDate = models.DateField(default=strftime("%Y-%m-%d"), name='endDate')

    def __str__(self):
        return str(self.user)









