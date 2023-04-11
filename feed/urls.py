from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('feed/', views.feed, name='feed'),  # 전체 피드
    path('feed/my_feed/<int:user>', views.user_feed,
         name='user_feed'),  # 마이페이지 피드
    path('feed/upload', views.upload_feed, name='upload_feed'),  # 게시글 삭제
    path('feed/my_feed/', views.upload_feed, name='upload_feed'),  # 게시글 삭제
    # 게시글 수정
    # path('posting/modify/', views.posting_modify, name='posting_modifiy'),
]
