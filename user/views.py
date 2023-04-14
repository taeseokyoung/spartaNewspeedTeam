from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse

def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = UserModel.objects.get(username=username)  # 사용자 불러오기
        if me.password == password:  # 저장된 사용자의 패스워드와 입력받은 패스워드 비교
            request.session['user'] = me.username  # 세션에 사용자 이름 저장
            return HttpResponse("로그인 성공!")
        else: # 로그인이 실패하면 다시 로그인 페이지를 보여주기
            return redirect('/sign-in')
    elif request.method == 'GET':
        return render(request, 'user/signin.html')



def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'user/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        bio = request.POST.get('bio', None)

        if password != password2:
            return render(request, 'user/signup.html')
        else:
            new_user = UserModel()
            new_user.username = username
            new_user.password = password
            new_user.bio = bio
            new_user.save()
        return redirect('/sign-in')