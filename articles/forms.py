from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label="title",
        widget=forms.TextInput(
            attrs={
                'max_length': 30,
                'class': '',
                'style': '',
                'placeholder': '제목을 입력하세요',
            }
        ),
        error_messages={
            'required': '나와라',
        }
    )
    content = forms.CharField(
        label="content",
        widget=forms.Textarea(
            attrs={
                'class': '',
                'style': '',
                'placeholder': '당신의 이야기를 들려주세요...',

            }
        )

    )

    class Meta:
        model = Article
        fields = '__all__'