from django.shortcuts import render, get_object_or_404
from .models import ClimbingArea, RockType
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def index(request):
    num_areas = ClimbingArea.objects.all().count()
    num_rock_types = RockType.objects.all().count()

    num_granite = ClimbingArea.objects.filter(rock_type__name__icontains='Granite').count()
    num_sand = ClimbingArea.objects.filter(rock_type__name__icontains="Sandstone").count()
    num_lime = ClimbingArea.objects.filter(rock_type__name__icontains="Limestone").count()

    num_beg = ClimbingArea.objects.filter(description__icontains="5.3").count()
    num_beg +=ClimbingArea.objects.filter(description__icontains="beginner").count()

    #Number of visits
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_areas': num_areas,
        'num_rock_types': num_rock_types,
        'num_granite': num_granite,
        'num_sand': num_sand,
        'num_lime': num_lime,
        'num_beg': num_beg,
        'num_visits': num_visits
    }


    return render(request, 'index.html', context=context)

from django.views import generic


class ClimbingAreaListView(generic.ListView):
    model = ClimbingArea
    context_object_name ='area_list'
    queryset = ClimbingArea.objects.all()

class ClimbingAreaDetailView(LoginRequiredMixin, generic.DetailView):
    model = ClimbingArea

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class AreaCreate(CreateView):
    model = ClimbingArea
    fields = ['area_name', 'type_of_climbing',
              'rock_type', 'description']
    
def search_areas(request):
    if request.method =="POST":
        searched = request.POST["searched"]
        areasN = ClimbingArea.objects.filter(area_name__contains=searched)
        areasR = ClimbingArea.objects.filter(rock_type__name__contains=searched)
        areasD = ClimbingArea.objects.filter(description__contains=searched)
        areasT = ClimbingArea.objects.filter(type_of_climbing__contains=searched)
        areas = areasN | areasR | areasD | areasT
        return render(request, 'climbingMap/search_areas.html',
                      {'searched':searched,
                        'areas':areas})
    else:
        return render(request, 'climbingMap/search_areas.html',)

