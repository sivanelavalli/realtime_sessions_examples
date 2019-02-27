from django.shortcuts import render
from django.utils import timezone
from datetime import date
from .models import Article,Reporter

def ArticleSubmit(request):
    fname = request.POST.get("n1")
    lname = request.POST.get("n2")
    email = request.POST.get("n3")
    r=Reporter(first_name=fname,last_name=lname,email=email)
    r.save()
    return render(request,"reporterlist.html")

def ReportsSubmit(request):
    id=request.POST.get("id1")
    head=request.POST.get("t1")
    pub_dte=request.POST.get("t2")
    new=Reporter.objects.get(pk=id)
    new1=Article(headline=head,pub_date=pub_dte,reporter=new)
    new1.save()
    data=new.article_set.all()
    return render(request,"repo_articles_list.html",{"msg":data})

def GotoArticles(request):
    return render(request,"reporterlist.html")
def AllPrevious_asper_time(request):
    newdata=Article.objects.filter(pub_date__lt=timezone.now())
    return render(request,"Art_asper_date.html",{"data":newdata})

def FutureArticles(request):
    f_articles=Article.objects.filter(pub_date__gt=timezone.now())
    return render(request,"future_articles.html",{"data":f_articles})
