from django.shortcuts import render,HttpResponse, Http404,  get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from .models import article,author,category, comment
from  django.contrib.auth.models import User
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from .form import createForm, registerUser ,createAuthor ,commentForm, categoryForm ,messageForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from django.contrib import messages



# Create your views here.


def index(request):
    post = article.objects.all().order_by('posted_on').reverse();


    #search = request.GET.get('q')
    #if search:
    #    post = post.filter(
    #       Q(title__icontains=search)|
    #        Q(body__icontains=search)

    #    )





    paginator = Paginator(post, 10)
    page = request.GET.get('page')
    total_article = paginator.get_page(page)

    catt=category.objects.all()


    context={
        "post": total_article,
        "catt": catt


    }

    return render(request, "index.html", context)



def getsingle(request, id):
    post= get_object_or_404(article, pk=id)
    first = article.objects.first()
    last = article.objects.last()
    commentt = comment.objects.filter(post=id)
    related = article.objects.filter(category=post.category).exclude(id=id)[:4]
    form = commentForm(request.POST or None)
    if form.is_valid():
        instancex = form.save(commit=False)
        instancex.post = post
        instancex.save()

    context={
        "post": post,
        "first": first,
        "last": last,
        "related": related,
        "form": form,
        "comment": commentt

    }
    return render(request, "single.html", context)

def getAuthor(request, name):

    post_author = get_object_or_404(User, username=name)
    auth= get_object_or_404(author, name=post_author.id)
    post = article.objects.filter(article_author=auth.id)
    context={
        "auth":auth,
        "post":post
    }

    return render(request, "profile.html", context)


def getTopic(request, name):
    cat=get_object_or_404(category,name=name)
    post=article.objects.filter(category=cat.id)

    context={
        "post": post,
        "cat": cat
    }
    return render(request, "category.html", context)


def getlogin(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            user = request.POST.get('user')
            password = request.POST.get('pass')
            auth = authenticate(request, username=user, password=password)

            if auth is not None:
                login(request, auth)
                return redirect('index')
            else:
                context={
                    'ok':"ak"
                }

                return render(request, "login.html", context)
    return render(request, "login.html")


def getlogout(request):
    logout(request)
    return redirect('index')

def getcreate(request):
    if request.user.is_authenticated:
        u = get_object_or_404(author, name=request.user.id)
        form = createForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instancex = form.save(commit=False)
            instancex.article_author = u
            instancex.save()

            return render(request,'index.html',{"ok": 1})
        return render(request, "create.html", {"form": form})
    else:
        return redirect('login')


def getprofile(request):
    if request.user.is_authenticated:

        user = get_object_or_404(User, id=request.user.id)
        author_profile = author.objects.filter(name=user.id)

        if author_profile:
            authorUser = get_object_or_404(author, name=request.user.id)
            post = article.objects.filter(article_author=authorUser.id)
            return render(request, "loginprofile.html", {"post": post, "user": authorUser})
        else:
            form=createAuthor(request.POST or None, request.FILES or None)
            if form.is_valid():
                instancex = form.save(commit=False)
                instancex.name=user
                instancex.save()
                return redirect('profile')
            return render(request,"createauthor.html", {"form": form})



    else:
        return redirect('login')


def getupdate(request, pid):
    if request.user.is_authenticated:
        u = get_object_or_404(author, name=request.user.id)
        post = get_object_or_404(article, id=pid)
        form = createForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            instancex = form.save(commit=False)
            instancex.article_author = u
            instancex.save()
            context={
                "ok":1
            }
            return render(request,"profile.html",context)
        return render(request, "create.html", {"form": form})
    else:
        return redirect('login')


def getdelete(request, id):
    if request.user.is_authenticated:
        post = get_object_or_404(article, id=id)
        post.delete()

        return render(request,'profile.html',{"ok2":1})
    else:
        return redirect("login")


def getregister(request):
    form = registerUser(request.POST or None)
    if form.is_valid():
            instancex =form.save(commit= False)
            instancex.save()
            context={
               "ok": 1
           }
            return render(request,'register.html',context)

    return render(request, "register.html", {"form": form})

def getcategory(request):
    cat = category.objects.all()
    context={
        "cat": cat
    }
    return render(request, "showcategory.html", context)

def addcategory(request):
    if request.user.is_authenticated:
        if request.user.is_staff or request.user.is_superuser:
            form = categoryForm(request.POST or None)
            if form.is_valid():
                instancex = form.save(commit=False)
                instancex.save()

                return render(request,'showcategory.html',{"ok": 1})

            return render(request, "addcategory.html", {"form": form})
        else:
            raise Http404('You are not authorised to access this page')
    else:
        return redirect('login')



def getcatupdate(request, name):

    cat = get_object_or_404(category, name=name)
    form = categoryForm(request.POST or None, instance=cat)
    if form.is_valid():
        instancex = form.save(commit=False)
        instancex.save()

        return render(request,"showcategory.html",{"ok2: 1"})
    return render(request, "addcategory.html", {"form": form})



def getcatdelete(request, name):

    cat = get_object_or_404(category, name=name)
    cat.delete()

    return render(request,"showcategory.html",{"ok3": 1})


def getmessage(request):
    form = messageForm(request.POST or None)
    if form.is_valid():
        instancex = form.save(commit=False)
        instancex.save()

        return render(request,'message.html',{"ok": 1})
    return render(request, "message.html", {"form": form})

def getsearch(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''
    post = article.objects.filter(title__contains=search_text).order_by('posted_on').reverse();
    return render(request, "searchResult.html", {"post": post})


def getchange(request):
    if request.method=='POST':
        form = PasswordChangeForm(data=request.POST,user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return render(request,'profile.html',{"ok3":2})

    else:
        form = PasswordChangeForm(user=request.user)
        context={
            "form": form
        }
        return render(request,"changePass.html",context)
