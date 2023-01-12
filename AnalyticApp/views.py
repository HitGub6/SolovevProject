from django.shortcuts import render
from .models import Data

# Create your views here.
def index(request):
    return render(request, 'index.html')

def demand(request):
    data = Data.objects.filter(name="Аналитик")[0]
    return render(request, 'demand.html', context={"graph": data.demand_graph.url, "table": str(data.demand_table)})

def geography(request):
    data = Data.objects.filter(name="Аналитик")[0]
    return render(request, 'geography.html', context={"graph": data.geography_graph.url, "table": str(data.geography_table)})