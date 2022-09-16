from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'articles'
urlpatterns = [
    # 메인 페이지
    path('', views.index, name='index'),
    # 글 작성
    path('create/', views.create, name='create'),
    # 검색
    path('search/', views.search, name='search'),
    # 디테일 페이지
    path('<int:pk>/detail/', views.detail, name='detail'),
    # 댓글 작성
    path('<int:pk>/detail/comment_create/', views.comment_create, name='comment_create'),
]

# MEDIA_URL로 들어오는 요청에 대해 MEDIA_ROOT 경로를 탐색한다.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)