from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

def record(request, record_id = 0):
    data = {
        'record': record_id,
        'view': 'Консультация',
        'nap' : 'Акушерство',
        'cost_o': '1200',
        'cost_t': '1500'
    }
    
    return render(request, 'index_record.html', data)

