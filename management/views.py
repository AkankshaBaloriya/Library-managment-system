from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Add


@login_required
def add(request):
    if request.method=='POST':
        name=request.POST.get("name")
        price=request.POST.get("price")
        author=request.POST.get("author")
        description=request.POST.get("description")
        image = request.FILES.get("image")
        AddBooks=Add(name=name, price=price, author=author, description=description, image=image)
        AddBooks.save()
        return HttpResponseRedirect('/')
        
    return render(request,'add_book.html')  

def book_details(request):
    if request.method == 'POST':
        if 'remove' in request.POST:
            book_name = request.POST.get('remove')
            book =Add.book_detail(book_name)
            book.delete()
            return redirect('home')
        
        elif "name" in request.POST:
            name1=request.POST.get('name')
            price1=request.POST.get('price')
            author1=request.POST.get('author')
            description1=request.POST.get('description')
            image1=request.FILES.get('image')
            print(name1)
            print(price1)
            print(author1)
            print(description1)
            print(image1)
            
            book=request.POST.get("book")
            
            change=Add.book_detail(book)
            change.name=name1
            change.price=price1
            change.author=author1
            change.description=description1
            change.image=image1
            change.save()
            
            
            return redirect('home')
            
    return render(request, 'home.html')

@login_required
def home(request):
    if request.method=="POST":
        name=request.POST.get('name')
        book_details=Add.book_detail(name)
        context={}
        context["context"]=book_details
        print(book_details.image.url)
        return render(request,"book_details.html",context)    
    else:    
        books=Add.showbook()
        context={}
        context["book"]=books
        return render(request, 'home.html',context)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message': error_message})
        
    return render(request, 'login.html')

def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeatPassword = request.POST['repeatPassword']

        if password == repeatPassword:
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
                login(request, user)
                return redirect('/login')
            except:
                error_mesage = 'Error creating account'
                return render(request, 'register.html', {'error_message' : error_mesage})
        else:
            error_mesage = 'Password do not match'
            return render(request, 'blog_generator/signup.html', {'error_message' : error_mesage})
    return render(request, 'register.html')