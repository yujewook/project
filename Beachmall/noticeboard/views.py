from django.shortcuts import render
from django.views.generic.base import View
from django.template import loader
from django.http.response import HttpResponse
from noticeboard.models import NoticeBoard
PAGE_SIZE = 5
PAGE_BLOCK = 5
# Create your views here.
class NoticeBoardListView(View):
    def get(self,request):
        template = loader.get_template("noticeboard.html")
        count = NoticeBoard.objects.all().count()
        #noticeboard.html에서 갖고오는 곳
        pagenum = request.GET.get("pagenoticenum")
        if not pagenum :
            pagenum = "1"
        pagenum = int(pagenum)
        
        # 밑에 바에서 보이는 것
        start = (pagenum - 1 ) *int(PAGE_SIZE) #(5-1)*10 +1 ->41
        end = start+ int(PAGE_SIZE)
        
        if end>count:
            end = count
            #전체글 다나옴 리스트로                         슬라이싱 0부터시작 하기 때문에 
        dtos = NoticeBoard.objects.order_by("-noticenum")[start:end]
        #페이지에서 글 번호 보여주는 것 
        number = count - (pagenum-1)*int(PAGE_SIZE)
        
        #페이지에 글 보여주게 하는것
        startpage = pagenum// int(PAGE_BLOCK) * int(PAGE_BLOCK) +1 
        if pagenum % int(PAGE_BLOCK) == 0:
            startpage -= int(PAGE_BLOCK)-1
        endpage =   startpage + int(PAGE_BLOCK) -1
        pagecount = count // int(PAGE_SIZE)
        if count % int(PAGE_SIZE)>0:
            pagecount +=1
        if endpage>pagecount :
            endpage = pagecount    
        pages = range(startpage , endpage+1)
        context = {
            "count" : count,
            "dtos" : dtos,
            "pagenum" : pagenum,
            "number":number,
            "pages":pages,
            "startpage":startpage,
            "endpage":endpage,
            "pageblock":PAGE_BLOCK,
            "pagecount":pagecount,
            }
        return HttpResponse( template.render( context, request ) )
    
    def post(self,request):
        pass
    
class NoticeDetailView(View):
    def get(self,request):
        noticenum = request.GET["noticenum"]
        pagenum = request.GET["pagenum"]
        number = request.GET["number"]
        dto = NoticeBoard.objects.get(noticenum=noticenum)
        context={
            "noticenum":noticenum,
            "pagenum":pagenum,
            "number":number,
            "dto":dto,
            }
        template = loader.get_template("noticedetail.html")
        return HttpResponse(template.render(context,request))
    
    def post(self,request):
        pass        