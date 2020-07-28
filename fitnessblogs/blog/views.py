from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from blog.models import Post, BlogComment
from django.contrib import messages
from blog.templatetags import extras

# Create your views here.

def blog(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blog/index.html', context)
    # return HttpResponse("We are in blogs")


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    post.views = post.views + 1
    post.save()
    comments = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}  #Blank dictionary in which all replies are stored and we fetch these replies with the help of template filter...
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]

        else:
            replyDict[reply.parent.sno].append(reply)
    # print(replyDict)    

    context = {'post':post, 'comments':comments, 'user':request.user, 'replyDict':replyDict} 
    return render(request, 'blog/blogpost.html', context)


def postComment(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        parentSno = request.POST.get("parentSno")
        post = Post.objects.get(post_id = postSno)
    if parentSno == "":    
        comment = BlogComment(comment=comment, user=user, post=post)
        comment.save()
        messages.success(request, "Your comment has been publish successfully")
    else:
        parent = BlogComment.objects.get(sno=parentSno)
        comment = BlogComment(comment=comment, user=user, post=post, parent = parent)
        comment.save()
        messages.success(request, "Your reply has been publish successfully")

    return redirect(f"/blog/{post.slug}")

 