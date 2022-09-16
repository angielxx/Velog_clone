from django import forms
from .models import Article, Comment

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

class CommentForm(forms.ModelForm):

    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': '댓글을 작성하세요.',
            }
        )
    )

    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ('article', 'user',)