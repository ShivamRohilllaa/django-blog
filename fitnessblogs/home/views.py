from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from home.models import Contact
from blog.models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request, 'home/index.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        if len(name)<2 or len(email)<2 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name = name, email = email, phone = phone, content = content )
            contact.save()
            messages.success(request, "Your message has been successfully sent.")

    return render(request, 'home/contact.html')

def search(request):
    query = request.GET['query']
    if len(query) > 80:
        allPosts = Post.objects.none()
    else:
        allPoststitle = Post.objects.filter(post_title__icontains = query)
        allPostscontent = Post.objects.filter(post_content__icontains = query)
        allPosts = allPoststitle.union(allPostscontent) 
        params = {'allPosts':allPosts, 'query':query}
    if allPosts.count() == 0:
        messages.warning(request, "No Result Found")    
    
    return render(request, 'home/search.html', params)



def about(request):
    return render(request, 'home/about.html')


def handleSignup(request):
    if request.method == 'POST':
    # GEt the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
    
    #check inputs
    if len(username) > 10:
        messages.error(request, "Enter valid username")
        return redirect('home')

    if not username.isalnum():
        messages.error(request, "Only Use Numbers & Letters")
        return redirect('home')

    if pass1 != pass2:
        messages.error(request, "Password do not match")
        return redirect('home')

    #Create the users
        myuser = User.objects.create_user(username, email, pass1 )
        myuser.first_name = fname
        myuser.Last_name = lname
        myuser.save()
        messages.success(request, "Your Account has been Successfully Created")
        return redirect('home')
    else:
        return HttpResponse('404 - Not Found')    


def handleLogin(request):
    loginusername = request.POST['loginusername']        
    loginpassword = request.POST['loginpassword']

    user = authenticate(username= loginusername, password= loginpassword)
    if user is not None:
        login(request, user)
        messages.success(request, "You are successfully logged in")
        return redirect('home')

    else:
        messages.error(request, "Please Enter Correct Username & Password")
        return redirect('home')

def handleLogout(request):
    logout(request)
    messages.success(request, "You are logged Out")
    return redirect('home')







