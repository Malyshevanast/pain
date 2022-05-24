from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .forms import *


def account (request):
    return render(request, 'account.html', {'heading': 'Создание','title': 'Создание'})

# ПОЛЬЗОВАТЕЛЬ
#Создание пользователя
def createUser (request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            User.objects.create(**form.cleaned_data)
    else:
        form = UserForm()
    user = User.objects.all()
    return render(request, "createUser.html", {"form": form, "user":user})

#Редактирование пользователя
def editUser(request, id):
    try:
        user = User.objects.get(id=id)
        if request.method == "POST":
            form = UserForm()
            user.first_name = request.POST.get("first_name")
            user.last_name = request.POST.get("last_name")
            user.patronymic = request.POST.get("patronymic")
            user.phone = request.POST.get("phone")
            user.save()
            return HttpResponseRedirect("/")
        else:
            form = UserForm() 
            return render(request, "editUser.html", {"form": form, "user": user})
    except User.DoesNotExist:
        return HttpResponseNotFound("<h2>User not found</h2>")

#Удаление пользователя
def deleteUser(request, id):
    try:
        user = User.objects.get(id=id)
        user.delete()
        return HttpResponseRedirect("/")
    except User.DoesNotExist:
        return HttpResponseNotFound("<h2>User not found</h2>")




# ЗАПИСЬ
#Создание записи    
def createRecord (request):
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            Record.objects.create(**form.cleaned_data)
    else:
        form = RecordForm()
    record = Record.objects.all()
    return render(request, "createRecord.html", {"form": form, "record": record})    

#Редактирование записи
def editRecord(request, id):
    try:
        record = Record.objects.get(id=id)
        if request.method == "POST":
            form = RecordForm()
            record.direction = request.POST.get("direction")
            record.service = request.POST.get("service")
            record.price = request.POST.get("price")
            record.data = request.POST.get("data")
            record.time = request.POST.get("time")
            record.save()
            return HttpResponseRedirect("/")
        else:
            form = RecordForm() 
            return render(request, "editRecord.html", {"form": form, "record": record})
    except Record.DoesNotExist:
        return HttpResponseNotFound("<h2>Record not found</h2>")

#Удаление записи
def deleteRecord(request, id):
    try:
        record = Record.objects.get(id=id)
        record.delete()
        return HttpResponseRedirect("/")
    except Record.DoesNotExist:
        return HttpResponseNotFound("<h2>Record not found</h2>")    
    
# УСЛУГА
#Создание услуги
def createService (request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            Service.objects.create(**form.cleaned_data)
    else:
        form = ServiceForm()
    service = Service.objects.all()
    return render(request, "createService.html", {"form": form, "service": service})

#Редактирование услуги
def editService(request, id):
    try:
        service = Service.objects.get(id=id)
        if request.method == "POST":
            form = ServiceForm()
            service.doctor = request.POST.get("doctor")
            service.text = request.POST.get("text")
            service.save()
            return HttpResponseRedirect("/")
        else:
            form = ServiceForm() 
            return render(request, "editService.html", {"form": form, "service": service})
    except Service.DoesNotExist:
        return HttpResponseNotFound("<h2>Service not found</h2>")

#Удаление услуги
def deleteService(request, id):
    try:
        service = Service.objects.get(id=id)
        service.delete()
        return HttpResponseRedirect("/")
    except Service.DoesNotExist:
        return HttpResponseNotFound("<h2>Service not found</h2>")
    
    
# ОТЗЫВЫ
#Создание отзыва
def createFeedback (request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            Feedback.objects.create(**form.cleaned_data)
        else: print("dsgfhj")
    else:
        form = FeedbackForm()
    feedback = Feedback.objects.all()
    return render(request, "createFeedback.html", {"form": form, "feedback": feedback})

#Редактирование отзыва
def editFeedback(request, id):
    try:
        feedback = Feedback.objects.get(id=id)
        if request.method == "POST":
            form = FeedbackForm()
            # feedback.author = request.POST.get("author")
            feedback.text = request.POST.get("text")
            feedback.time_create = request.POST.get("time_create")
            feedback.time_update = request.POST.get("time_update")
            # feedback.tour = request.POST.get("tour")
            feedback.save()
            return HttpResponseRedirect("/")
        else:
            form = FeedbackForm() 
            return render(request, "editFeedback.html", {"form": form, "tour" : feedback})
    except Feedback.DoesNotExist:
        return HttpResponseNotFound("<h2>Feedback not found</h2>")

#Удаление отзыва
def deleteFeedback(request, id):
    try:
        feedback = Feedback.objects.get(id=id)
        feedback.delete()
        return HttpResponseRedirect("/")
    except User.DoesNotExist:
        return HttpResponseNotFound("<h2>Feedback not found</h2>")    
    
# Карта
#Создание карты
def createCard (request):
    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            Card.objects.create(**form.cleaned_data)
    else:
        form = CardForm()
    сard = Card.objects.all()
    return render(request, "createCard.html", {"form": form, "сard":сard})

#Редактирование карты
def editCard(request, id):
    try:
        сard = Card.objects.get(id=id)
        if request.method == "POST":
            form = CardForm()
            сard.policy = request.POST.get("policy")
            сard.bobo = request.POST.get("bobo")
            сard.save()
            return HttpResponseRedirect("/")
        else:
            form = CardForm() 
            return render(request, "editCard.html", {"form": form, "сard": сard})
    except Card.DoesNotExist:
        return HttpResponseNotFound("<h2>сard not found</h2>")

#Удаление карты
def deleteCard(request, id):
    try:
        сard = Card.objects.get(id=id)
        сard.delete()
        return HttpResponseRedirect("/")
    except User.DoesNotExist:
        return HttpResponseNotFound("<h2>сard not found</h2>")
