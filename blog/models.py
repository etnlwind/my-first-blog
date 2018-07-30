from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # models.ForeignKey - 다른 모델에 대한 링크
    title = models.CharField(max_length=200)  # models.CharField - 글자 수가 제한된 텍스트를 정의할 때 사용
    text = models.TextField() # models.TextField - 글자 수에 제한이 없는 긴 텍스트
    created_date = models.DateTimeField(default=timezone.now)  # models.DateTimeField - 날짜와 시간
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):  # __str__를 호출하면 Post 모델의 제목 텍스트(string)를 얻게 될 거에요.
        return self.title
