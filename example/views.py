from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
import requests
from pprint import pprint
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('example.view_example')
def index(request):
    
    # try to fetch demo the data
    try:        
        headers = {
            'Cache-Control': 'max-age=3600',
            'Accept': 'application/json'
        }
        r = requests.get(
            url="https://restcountries.eu/rest/v2/all",
            headers=headers
        )
        r.raise_for_status()
        countries = r.json()
    
    except:
        raise Http404("Network error occurred when trying to connect to API")
    
    template = loader.get_template('example/index.html')
    context = {
        'countries': countries
    }    
    return HttpResponse(template.render(context, request))
