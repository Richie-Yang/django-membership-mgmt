from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Six(models.Model):
    # 分數區間的頭
    range_start = models.IntegerField(default=0)
    # 分數區間的尾
    range_end = models.IntegerField(default=0)
    grade = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='grade_pictures', default="")
