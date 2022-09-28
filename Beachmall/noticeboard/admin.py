from django.contrib import admin
from noticeboard.models import NoticeBoard

# Register your models here.
class NoticeBoardAdmin(admin.ModelAdmin):
    list_play=("noticenum","admin"," noticetitle",
               "noticecontent","noticedate")

admin.site.register(NoticeBoard , NoticeBoardAdmin)