from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse

from .forms import *

from .models import Poem, User
from django.core.paginator import Paginator


def index(request):
    """This view displays all poems posted"""
    poems = Poem.objects.all()    # Gets poems
    paginator = Paginator(poems, 8) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "poetica/index.html", {"page_obj": page_obj})


def post_poem(request):
    """This view lets the user post a poem"""
    if request.method == "POST":  
        form = PostPoem(request.POST)   
        if form.is_valid():  
            poem = form.save(commit=False)
            poem.poster = request.user    # The user is set as the author of the poem
            poem.save()
            return HttpResponseRedirect(reverse("index"))    # Redirects to the index page

    form = PostPoem() 
    return render(
        request,   
        "poetica/post_poem.html",   
        {
            "form": form,
        },
    )


def profile(request, user_id):
    """This view displays the profile page of the user"""
    
    current_user = User.objects.get(id=user_id)
    poems = Poem.objects.filter(poster=user_id)  # Gets poems by the user
    paginator = Paginator(poems, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    form = WriteStatus()

    # Processes submitted status update
    if request.method == "POST" and "write_status" in request.POST:
        form = WriteStatus(request.POST)
        if form.is_valid():
            status = form.save(commit=False)
            status.poet = request.user   # The current user is set as the author of the status
            status.save()
            return HttpResponseRedirect(reverse("profile", kwargs={"user_id": user_id}))   # Refreshes the profile page
    if current_user.users_status.all().count() == 0: 
        status = "No current status" # If the user doesn't have a status message, default message is displayed
    else:
        status = current_user.users_status.last().status_body # The most recent status message is displayed

    return render(
        request,
        "poetica/profile.html",
        {
            "current_user": current_user,
            "page_obj": page_obj,
            "status": status,
            "form": form,
        },
    )


def poem_page(request, poem_id):
    """This view displays a page for an individual poem"""
    poem = Poem.objects.get(id=poem_id)  # Gets the poem
    form = WriteComment()

    # Processes posted comment
    if request.method == "POST" and "write_comment" in request.POST:
        form = WriteComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.commenter = request.user
            comment.poem = poem
            comment.save()
            return HttpResponseRedirect(
                reverse("poem_page", kwargs={"poem_id": poem_id}) # Refreshes the poem page
            )
    return render(
        request,
        "poetica/poem_page.html",
        {"poem": poem, "comments": poem.poem_comments.all(), "form": form},
    )


def like_poem(request, poem_id):
    """This view adds a like to a poem from the current user"""
    poem = Poem.objects.get(id=poem_id)
    poem.likes.add(request.user)    # Adds the current user's like
    poem.save()
    likes_count = poem.likes.all().count()    # Stores the number of likes a poem has
    return JsonResponse({"likes_count": likes_count}) 


def unlike_poem(request, poem_id):
    """This view removes a like for a poem"""
    poem = Poem.objects.get(id=poem_id)
    poem.likes.remove(request.user)    # Removes the current user's like
    poem.save()
    likes_count = poem.likes.all().count()    # Stores the number of likes a poem has
    return JsonResponse({"likes_count": likes_count})


def delete_poem(request, poem_id):
    """This view lets a user delete a poem"""
    if request.method == "POST":
        poem = Poem.objects.get(id=poem_id)
        poem.delete()
        return HttpResponseRedirect(reverse("index"))    


def liked_poems(request):
    """This view displays the poems that the user has liked"""
    current_user = User.objects.get(id=request.user.id)
    liked_poems = current_user.poems_liked.all()  # Retrieves the poems liked by the user
    paginator = Paginator(liked_poems, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "poetica/likes.html", {"page_obj": page_obj})


def poets(request):
    """This view displays the poets with accounts on the site"""
    poets = User.objects.all()
    paginator = Paginator(poets, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "poetica/poets.html", {"page_obj": page_obj})
