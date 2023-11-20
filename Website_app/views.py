from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    #Testing.
    #print("TESTING: All students with shows: ", Student.objects.select_related('show'))

    

    return render( request, 'Website_app/index.html', {'shows':shows})

def unfinishedShowList(request):
    #Testing.
    #print("TESTING: All students with shows: ", Student.objects.select_related('show'))
    unfinished_shows = Show.objects.all().filter(finished = False)
    print("show query set", unfinished_shows)
    return render( request, 'Website_app/show_list_unfinished.html', {'unfinished_shows':unfinished_shows})

class ShowDetailView(generic.DetailView):
    model = Show
class ShowListView(generic.ListView):
    model = Show

def createShow(request):
    form = ShowForm()
    
    if request.method == 'POST':
        # Create a new dictionary with form data and show_id
        show_data = request.POST.copy()
        
        form = ShowForm(show_data)
        if form.is_valid():
            # Save the form without committing to the database
            show = form.save(commit=False)
            
            show.save()

            # Redirect back to the show detail page
            return redirect('show-list')

    context = {'form':form}
    return render(request, 'Website_app\show_form.html', context)

def updateShow(request, show_id):
    show = Show.objects.get(id = show_id)
    form = ShowForm(instance=show)

    if request.method == 'POST':
        # Retrieve the show based on the show_id
        print('printing POST:', request.POST)
        print('Show id:', show_id)
        form = ShowForm(request.POST, instance=show)
        
        if form.is_valid():
            # Save the form without committing to the database
            show = form.save(commit=False)

            show.save()
            # Redirect back to the show detail page
            return redirect('show-detail', show_id)


    context = {'form': form}
    return render(request, 'Website_app/Show_form.html',context )

def deleteShow(request, show_id):
    show = Show.objects.get(id = show_id)

    if request.method == "POST":
        show.delete()
        messages.success(request, "The show has been deleted.")
        
        return redirect('show-list')

    context = {"show": show}
    return render(request, 'Website_app/show_delete.html',context )

def UserDetailView(request, user_id):

    shows = None
    shows = Show.objects.all().filter(user = user_id)
    if request.GET.get("Show_types"):
        results = request.GET.get("Show_types")
        print(results)
        if results == "Unfinished":
            shows = shows.filter(finished = False)
        elif results == "Finished":
            shows = shows.filter(finished = True)

    user = User.objects.get(id = user_id)
    return render( request, 'Website_app/user_detail.html', {'user': user, 'shows':shows})