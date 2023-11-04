from django.shortcuts import render, redirect
from django.views import generic
from .models import *
from .forms import *

# Create your views here.
def index(request):
    #Testing.
    #print("TESTING: All students with shows: ", Student.objects.select_related('show'))
    all_shows = Show.objects.all()
    print("show query set", all_shows)
    return render( request, 'Website_app/index.html', {'shows':all_shows})

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