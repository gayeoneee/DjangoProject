from django import forms
from .models import Post    #같은 폴더 안의 models 중 Post 모델 불러오기기

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']  # 입력받을 필드를 정의

