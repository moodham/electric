from django.urls import path, include

from .views import blogs, blog, page_number, home, article, h , tells , tell,tells_page_number,antenna,antenas,antenas_page_number




urlpatterns = [
    path("", home, name="home"),


    path("tell/<slug>", tell, name="tell"),
    path("tells", tells, name="tells"),
    path("tells/<pagenumbers>", tells_page_number, name="tells_page-number"),
    
    path("antena/<slug>", antenna, name="antena"),
    path("antenas", antenas, name="antenas"),
    path("antenas/<pagenumbers>", antenas_page_number, name="antenas_page-number"),
    
    
    path("blog/<slug>", blog, name="blog name"),
    path("blogs", blogs, name="blogs name"),
    path("blogs/<pagenumbers>", page_number, name="page-number"),
    path("article/<slug>", article, name="article"),


    path("1", h.as_view(), name="h")]