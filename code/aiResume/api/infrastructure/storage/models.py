from django.db import models

class QuestionModel(models.Model):
    id = models.CharField(max_length=26, primary_key=True)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    computingTokens = models.IntegerField()
    completionTokens = models.IntegerField()
    totalTokens = models.IntegerField()

    def __str__(self):
        return self.question
    
