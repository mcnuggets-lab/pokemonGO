from django.shortcuts import render
#from django.http import JsonResponse

import math, sys, random
from . import cpvhp as test1

# Create your views here.

def index(request):
    context = {
        'title': 'To be constructed',
    }
    return render(request, 'pokemonGO/index.html', context)
    


def cpvhp(request):
    context = {
        'title': 'Pokemon max CP vs max HP',
        'data': {
            'names' : test1.names,
            'types' : test1.types,
            'typeColors' : test1.type_colors,
            'mcp' : test1.mcp,
            'mhp' : test1.mhp
            }
    }
    return render(request, 'pokemonGO/cpvhp.html', context)
    


    

    
