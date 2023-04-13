from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post

# 로그인한 사용자들의 피드가 최신순으로 조회되어야 한다.
# 모든 비로그인 방문자들도 메인 피드를 구경할 수 있어야 한다.


def home(request):
    if request.method == 'GET':
        all_feed = Post.objects.all().order_by('-created_at')
        return render(request, 'feed/feed.html', {'tweet': all_feed})


# 메인 피드에 전체 게시글을 보여준다. : GET
def feed(request):
    if request.method == 'GET':
        all_feed = Post.objects.all().order_by('-created_at')
        return render(request, 'feed/feed.html', {'tweet': all_feed})


# 마이페이지(로그인한 사용자들) 에 자신이 작성한 피드를 불러올 함수. : GET
@login_required
def user_feed(request):
    if request.method == 'GET':
        # 사용자가 로그인 되었는지(인증된 사용자가 있는지)
        # user = request.user.is_authenticated
        if user:
            my_post = Post.objects.get(user=user).order_by('-created.at')
            return render(request, 'feed/my_feed.html', {'feed': my_post})
            # 연결할 때 3강 4:25 부분 참고하기


# 로그인 사용자들이 피드 업로드 시 저장해주는 함수. : POST
@login_required
def upload_feed(request):
    if request.method == 'GET':
        return render(request, 'base.html')
    if request.method == 'POST':
        # user = request.user
        my_post = Post()
        # my_post.author = user

        # request.POST.get('html의 각각의 태그 name이 여기에 적힙니다','')
        my_post.post_title = request.POST.get('subject', None)
        my_post.post_content = request.POST.get('contents', None)
        #my_post.post_image = request.POST.get('imageUrl', None)
        my_post.save()
        return redirect('/feed/detail')


# 로그인한 사용자들이 자신의 피드를 삭제할 함수.
@login_required
def delete_feed(request, id):
    my_feed = Post.objects.get(id=id)
    my_feed.delete()
    return redirect('/feed')

@login_required
def modify_feed(request, id):
    if request.method == 'GET':
        return render(request, 'feed/feed_detail.html')
    if request.method == 'POST':
        my_post = Post.objects.get(id=id)
        my_post.post_title = request.POST.get('subject', None)
        my_post.post_content = request.POST.get('contents', None)
        my_post.post_image = request.POST.get('imageUrl', None)
        my_post.save()
        return redirect('/feed')
    
@login_required
def modify_feed(request):
    if request.method == 'GET':
        all_feed = Post.objects.all().order_by('-created_at')
        return render(request, 'feed/feed_detail.html',{'post':all_feed[0]})
    if request.method == 'POST':
        # my_post = Post.objects.get(id=id)
        # my_post.post_title = request.POST.get('subject', None)
        # my_post.post_content = request.POST.get('contents', None)
        # my_post.post_image = request.POST.get('imageUrl', None)
        # my_post.save()
        return redirect('/feed')
    
