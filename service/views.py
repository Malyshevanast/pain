from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
 

def info(request, info_id = 1):
    data = {
        'number': info_id,
        'detail': 'Акушерство',
        'address': 'г. Владимир, ул. Чертаново, корпус 7',
        'record': [
            {'id': 1}
        ]
    }
    return render(request, 'index_service.html', data)
