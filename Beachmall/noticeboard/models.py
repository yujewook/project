from django.db import models

# Create your models here.
class NoticeBoard(models.Model):
    noticenum = models.AutoField(verbose_name="공지글 번호", primary_key=True)
    admin =  models.CharField(max_length=30,verbose_name="작성자",null=False)
    noticetitle = models.CharField(max_length=1000,verbose_name="공지글 제목",null=False)
    noticecontent = models.CharField(max_length=6000,verbose_name="공지글 내용",null=False)
    noticedate = models.DateTimeField(auto_now_add=True,verbose_name="작성일",blank=True)