from django.shortcuts import render
from django.views.generic.base import View
from django.template import loader
from django.http.response import HttpResponse
from product.models import Product
import logging
from product.choice import BRAND_CHOICE

# Create your views here.
logger = logging.getLogger( __name__ )

PAGE_SIZE = 15
PAGE_BLOCK = 5
    
class ProductDetailView(View):
    def get(self, request):
        template = loader.get_template("productDetail.html")
        prodNum = request.GET["prodNum"]
        product = Product.objects.get(prodNum=prodNum)
        context = {
            "product" : product
            }
        print(product.brand)
        return HttpResponse(template.render(context, request))
    def post(self, request):
        pass
    
class ProductCategoryView(View):
    def get (self,request):
        template=loader.get_template("productCategory.html")
        context={
            "brands" : BRAND_CHOICE,
            }
        return HttpResponse(template.render( context ,request))
    def post(self,request):
        pass
    
class WaterRocketView(View):
    def get (self,request):
        context={}
        template=loader.get_template("waterRocket.html")
        return HttpResponse(template.render( context ,request))
    def post(self,request):
        pass
    
class ProductListView(View):
    def get (self,request):
        template = loader.get_template( "productList.html" )
        
        brand = request.GET["brand"]
        
        count = Product.objects.filter(brand=brand).count()
        
        pagenum = request.GET.get( "pagenum" )
        if not pagenum :
            pagenum = "1"
        pagenum = int( pagenum )
        
        start = ( pagenum - 1 ) * int(PAGE_SIZE)          # ( 5 - 1 ) * 10 + 1     41
        end = start + int(PAGE_SIZE)                      # 41 + 10 - 1            50
        if end > count :
            end = count
        products = Product.objects.filter(brand=brand).order_by("-prodNum" )[start:end] # jsp와 다르게 슬라이싱해서 씀
        number = count - ( pagenum - 1 ) * int(PAGE_SIZE )
        
        startpage = pagenum // int(PAGE_BLOCK) * int(PAGE_BLOCK) + 1       # 9 // 10 * 10 + 1    1
        if pagenum % int(PAGE_BLOCK) == 0:
            startpage -= int(PAGE_BLOCK)
        endpage = startpage + int(PAGE_BLOCK) - 1                         # 1 + 10 -1           10
        pagecount = count // int(PAGE_SIZE)
        if count % int(PAGE_SIZE) > 0 :
            pagecount += 1
        if endpage > pagecount :
            endpage = pagecount
        pages = range( startpage, endpage+1 )
        context = {
            "brands" : BRAND_CHOICE,
            "count" : count,
            "products" : products,
            "pagenum" : pagenum,
            "number" : number,
            "pages" : pages,
            "startpage" : startpage,
            "endpage" : endpage,
            "pageblock" : PAGE_BLOCK,
            "pagecount" : pagecount,
            }
        return HttpResponse(template.render( context, request))
    def post(self,request):
        pass

