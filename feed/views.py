from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Post

# Create your views here.


# 피드 홈에서는 로그인한 사용자들의 피드가 최신순으로 조회되어야 한다.
# 모든 비로그인 방문자들도 메인 피드를 구경할 수 있어야 한다.
# def home(request):
#     return redirect('/feed')

# 메인 피드에 전체 게시글을 보여준다. : GET
def feed(request):
    if request.method == 'GET':
        all_feed = Post.objects.all().order_by('-created_at')
        return render(request, 'tweet/feed.html', {'tweet':all_feed})


# 로그인 사용자들이 피드 업로드 시 저장해주는 함수. : POST
@login_required
def upload_feed(request):
    if request.method == 'POST':
        # uset = request.user
       my_post = Post()
        # my_post.author = user

        # request.POST.get('html의 각각의 태그 name이 여기에 적힙니다','')
       my_post.post_title = request.POST.get('','')
       my_post.post_content = request.POST.get('','')
       my_post.post_image = request.POST.get('','')
       my_post.save()
       return redirect('/feed')


# 마이페이지(로그인한 사용자들) 에 자신이 작성한 피드를 불러올 함수. : GET
 
@login_required
def user_feed(request):
    if request.method == 'GET':
        # 사용자가 로그인 되었는지(인증된 사용자가 있는지)
        # user = request.user.is_authenticated
        if user:
            my_post = Post.objects.


# @login_required
# def delete_feed():


