from django.shortcuts import render
from django.views import generic
from .models import *

# Create your views here.
def index(request):
    #Testing.
    #print("TESTING: All students with portfolios: ", Student.objects.select_related('portfolio'))
    all_portfolios = Show.objects.all()
    print("show query set", all_portfolios)
    return render( request, 'Website_app/index.html', {'portfolios':all_portfolios})

class ShowDetailView(generic.DetailView):
    model = Show
class ShowListView(generic.ListView):
    model = Show