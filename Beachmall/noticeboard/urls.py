from django.urls.conf import path
from noticeboard import views

urlpatterns=[
   path("noticelist",views.NoticeBoardListView.as_view(), name="noticelist"),
   path("noticedetail",views.NoticeDetailView.as_view(), name="noticedetail"),
       
    ]