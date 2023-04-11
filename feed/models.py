from django.db import models

# Create your models here.
class Post(models.Model):
    class Meta:
        db_table ="my_post"
   
    post_title = models.TextField(default = "write title") #게시글 제목
    post_content = models.TextField(default = "write content") #게시글 내용
    post_image = models.TextField(default = "image url")
    created_at = models.DateTimeField(auto_now_add=True) # 생성시간
    updated_at = models.DateTimeField(auto_now=True) # 수정시간
    
    # user_nickname = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    # user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
