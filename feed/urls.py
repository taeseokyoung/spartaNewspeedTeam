from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # 04.11. 서경 url 연결
    path('admin/', admin.site.urls),
    # path('/', views.home, name='home'),  # 홈 화면
    path('', include('user.urls')),
    path('feed/', views.feed, name='feed'),  # 로그인한 사용자의 홈 화면

    path('feed/detail/delete/<int:id>', views.delete_feed, name='delete'),  # 게시글 삭제
    path('my_feed', views.user_feed, name='user_feed'),  # 마이페이지 및 프로필 수정

    # 기호님 게시글 수정
    # path('feed/modify/', views.modify_feed, name='modifiy'),
    path('feed/detail/<int:id>', views.modify_feed, name='detail'),  # 상세보기 및 수정
    #### upload_feed에서 modify_feed로변경
    path('feed/upload/', views.upload_feed, name='upload'), #업로드 피드


]
