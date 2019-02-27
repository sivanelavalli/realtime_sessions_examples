from django.db import models


class Question(models.Model):
    id=models.IntegerField(primary_key=True)
    question_text=models.CharField(max_length=400)
    pub_date=models.DateTimeField(auto_now=True)