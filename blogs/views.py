from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import posts, Article, comments,Netposts,antena
from django.shortcuts import render
from .form import commentform
import urllib


# class home(TemplateView):
#    template_name = "index.html"

def tells(request):
    context = Netposts.objects.all().order_by("id")
    a = int(context.count() / 6)
    print(a)
    print(context.count())
    a = range(0, a + 1)
    print(a)
    x = range(6, context.count()+1, 6)
    page_title = "تمامی مطالب تلفن سانترال"
    print(x)
    x = {k: v+1 for k, v in zip(x, a)}
    print(type(x), x)
    print(a)
    print(len(context))
    return render(request, "tells.html", {"context": context, "x": x, "page_title": page_title})

def tells_page_number(request, pagenumbers):
    print(pagenumbers)
    pagenumbers = int(pagenumbers)
    print(pagenumbers)
    context = Netposts.objects.all().order_by("id")
    entry_list = list(context)

    print(context)
    print(context[0])

    print(entry_list)
    print(entry_list[0])
    print(type(entry_list))

    print(posts.objects.count())

    context = entry_list[pagenumbers-1:pagenumbers+5]
    print(context)
    pagenumbers1 = pagenumbers + 1
    pagenumbers2 = pagenumbers + 2
    pagenumbers3 = pagenumbers + 3
    pagenumbers4 = pagenumbers + 4
    pagenumbers5 = pagenumbers + 5
    page_title = "صفحه مطالب  تلفن سانترال-"+str(pagenumbers/6)

    return render(request, "tells2.html", {"context": context, "page_title": page_title, "pagenumbers": pagenumbers, "pagenumbers1": pagenumbers1, "pagenumbers2": pagenumbers2, "pagenumbers3": pagenumbers3, "pagenumbers4": pagenumbers4, "pagenumbers5": pagenumbers5})


def tell(request, slug):
    print(slug)
    slug=urllib.parse.unquote(slug)
    context = Netposts.objects.filter(post_title=slug)
    for i in context:

        print(i.pk, "contextcontextcontextcontextcontextcontext")
    comment = comments.objects.filter(post_id=context[0].pk, approved= True)

    page_title = slug

    print(Netposts.objects.count())

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = commentform(request.POST)
        # check whether it's valid:
        print(request.META['REMOTE_ADDR'])
        if form.is_valid():
            cd = form.cleaned_data
            comments.objects.create(
                author_name=cd['name'], author_email=cd['sender'], content=cd['message'], post_id=context[0].pk, author_ip=request.META['REMOTE_ADDR'])

            # process the data in form.cleaned_data as required
            # ...

            return render(request, "tell.html", {"context": context, "context0": context[0], "page_title": page_title, "comment": comment, 'form': commentform()})

    # if a GET (or any other method) we'll create a blank form
    else:

        return render(request, "tell.html", {"context": context, "context0": context[0], "page_title": page_title, "comment": comment, 'form': commentform()})


def home(request):

    context2 = posts.objects.all().order_by("id")
    a = int(context2.count())
    context = posts.objects.all()[a-6:a]
    a = int(context.count())
    print(posts.objects.count())
    print(context)
    return render(request, "index.html", {"context": context})

#************************************************************************************************************************************************************
def antenas(request):
    context = antena.objects.all().order_by("id")
    a = int(context.count() / 6)
    print(a)
    print(context.count())
    a = range(0, a + 1)
    print(a)
    x = range(6, context.count()+1, 6)
    page_title = "تمامی مطالب آنتن مرکزی"
    print(x)
    x = {k: v+1 for k, v in zip(x, a)}
    print(type(x), x)
    print(a)
    print(len(context))
    return render(request, "antenas.html", {"context": context, "x": x, "page_title": page_title})

def antenas_page_number(request, pagenumbers):
    print(pagenumbers)
    pagenumbers = int(pagenumbers)
    print(pagenumbers)
    context = antena.objects.all().order_by("id")
    entry_list = list(context)

    print(context)
    print(context[0])

    print(entry_list)
    print(entry_list[0])
    print(type(entry_list))

    print(antena.objects.count())

    context = entry_list[pagenumbers-1:pagenumbers+5]
    print(context)
    pagenumbers1 = pagenumbers + 1
    pagenumbers2 = pagenumbers + 2
    pagenumbers3 = pagenumbers + 3
    pagenumbers4 = pagenumbers + 4
    pagenumbers5 = pagenumbers + 5
    page_title = "صفحه مطالب  آنتن مرکزی-"+str(pagenumbers/6)

    return render(request, "antenas2.html", {"context": context, "page_title": page_title, "pagenumbers": pagenumbers, "pagenumbers1": pagenumbers1, "pagenumbers2": pagenumbers2, "pagenumbers3": pagenumbers3, "pagenumbers4": pagenumbers4, "pagenumbers5": pagenumbers5})


def antenna(request, slug):
    print(slug)
    slug=urllib.parse.unquote(slug)
    context = antena.objects.filter(post_title=slug)
    for i in context:

        print(i.pk, "contextcontextcontextcontextcontextcontext")
    comment = comments.objects.filter(post_id=context[0].pk, approved= True)

    page_title = slug

    print(antena.objects.count())

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = commentform(request.POST)
        # check whether it's valid:
        print(request.META['REMOTE_ADDR'])
        if form.is_valid():
            cd = form.cleaned_data
            comments.objects.create(
                author_name=cd['name'], author_email=cd['sender'], content=cd['message'], post_id=context[0].pk, author_ip=request.META['REMOTE_ADDR'])

            # process the data in form.cleaned_data as required
            # ...

            return render(request, "antena.html", {"context": context, "context0": context[0], "page_title": page_title, "comment": comment, 'form': commentform()})

    # if a GET (or any other method) we'll create a blank form
    else:

        return render(request, "antena.html", {"context": context, "context0": context[0], "page_title": page_title, "comment": comment, 'form': commentform()})



#**************************************************************************************
class h(TemplateView):
    template_name = "i.html"


def blog(request, slug):
    print(slug)
    slug=urllib.parse.unquote(slug)
    context = posts.objects.filter(post_title=slug)
    for i in context:

        print(i.pk, "contextcontextcontextcontextcontextcontext")
    comment = comments.objects.filter(post_id=context[0].pk, approved= True)

    page_title = slug

    print(posts.objects.count())

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = commentform(request.POST)
        # check whether it's valid:
        print(request.META['REMOTE_ADDR'])
        if form.is_valid():
            cd = form.cleaned_data
            comments.objects.create(
                author_name=cd['name'], author_email=cd['sender'], content=cd['message'], post_id=context[0].pk, author_ip=request.META['REMOTE_ADDR'])

            # process the data in form.cleaned_data as required
            # ...

            return render(request, "blog.html", {"context": context, "context0": context[0], "page_title": page_title, "comment": comment, 'form': commentform()})

    # if a GET (or any other method) we'll create a blank form
    else:

        return render(request, "blog.html", {"context": context, "context0": context[0], "page_title": page_title, "comment": comment, 'form': commentform()})



def article(request, slug):
    print(slug)
    slug=urllib.parse.unquote(slug)
    print(slug)
    context = Article.objects.filter(post_title=slug)
    entry_list = list(context)
    page_title = slug
    print(context)
    print(entry_list)
    print(Article.objects.count())

    return render(request, "article.html", {"context": context[0], "page_title": page_title})


def blogs(request):
    context = posts.objects.all().order_by("id")
    a = int(context.count() / 6)
    print(a)
    print(context.count())
    a = range(0, a + 1)
    print(a)
    x = range(6, context.count()+1, 6)
    page_title = "تمامی مطالب تابلو برق پریس"
    print(x)
    x = {k: v+1 for k, v in zip(x, a)}
    print(type(x), x)
    print(a)
    print(len(context))
    return render(request, "blogs.html", {"context": context, "x": x, "page_title": page_title})


def page_number(request, pagenumbers):
    print(pagenumbers)
    pagenumbers = int(pagenumbers)
    print(pagenumbers)
    context = posts.objects.all().order_by("id")
    entry_list = list(context)

    print(context)
    print(context[0])

    print(entry_list)
    print(entry_list[0])
    print(type(entry_list))

    print(posts.objects.count())

    context = entry_list[pagenumbers-1:pagenumbers+5]
    print(context)
    pagenumbers1 = pagenumbers + 1
    pagenumbers2 = pagenumbers + 2
    pagenumbers3 = pagenumbers + 3
    pagenumbers4 = pagenumbers + 4
    pagenumbers5 = pagenumbers + 5
    page_title = "صفحه مطالب برقکار شماره-"+str(pagenumbers/6)

    return render(request, "blogs2.html", {"context": context, "page_title": page_title, "pagenumbers": pagenumbers, "pagenumbers1": pagenumbers1, "pagenumbers2": pagenumbers2, "pagenumbers3": pagenumbers3, "pagenumbers4": pagenumbers4, "pagenumbers5": pagenumbers5})


print("sport ")
















