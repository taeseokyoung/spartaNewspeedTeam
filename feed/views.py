from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Post
# Create your views here.


# 피드 홈에서는 로그인한 사용자들의 피드가 최신순으로 조회되어야 한다.
# 모든 비로그인 방문자들도 메인 피드를 구경할 수 있어야 한다.
def home(request):
    return redirect('/feed')

# GET : 메인 피드에 전체 게시글을 보여준다.
def feed(request):
    if request.method == 'GET':
        all_feed = Post.objects.all().order_by('_created_at')
        return render(request, 'tweet/feed.html'), {'tweet':all_feed}


# @login_required
# def upload_feed(request)
    
# @login_required
# def delete_feed()
