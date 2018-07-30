
# 프로젝트 생성
mkdir djangogirls
cd djangogirls
python3 -m venv myvenv
sudo apt install python-virtualenv
virtualenv --python=python3.6 myvenv
source myvenv/bin/activate
python3 -m pip install --upgrade pip
pip3 install django

django-admin startproject mysite .
mysite/settings.py
ALLOWED_HOSTS = ['127.0.0.1', 'api.magibase.com']
TIME_ZONE = 'Asia/Seoul'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

python3 manage.py migrate
python3 manage.py runserver 0:8000



python3 manage.py startapp blog
vi mysite/settings.py
INSTALLED_APPS = [
    . . .
    'blog',
]

blog/models.py 파일을 열어서 안에 모든 내용을 삭제한 후 아래 코드를 추가하세요.
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



python3 manage.py makemigrations blog   	# 장고 모델을 변경후에 DB에 반영할 수 있도록 migration file 생성
python3 manage.py migrate blog		        # migration file을 사용하여 실제 DB에 반영

# 이제 blog/admin.py 파일을 열어서 내용을 다음과 같이 바꾸세요.
from django.contrib import admin
from .models import Post

admin.site.register(Post)


python3 manage.py createsuperuser
