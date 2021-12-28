from django.shortcuts import render 
from django.http import JsonResponse ,HttpResponse
from .models import note 
from django.http import request
from django.contrib.auth.models import User

def show_my_note(request):
    if request.method=='GET':
        author=request.user.id
        qs=list(note.objects.filter(id=author).values())
        return JsonResponse({'data :': qs})

def show_all_note(request):
    if request.method=='GET':
        qs=list(note.objects.values())
        return JsonResponse({'data :': qs})

def update(request,id,text):
    if request.method=='GET':
        qs=note.objects.filter(id=id).update(note=text)
        return HttpResponse('successfull')

def delet(request,id):
    if request.method=='GET':
        qs=note.objects.filter(id=id).delete()
        return HttpResponse('successfull')

def send(request,who,note):
    qs=list(note.objects.filter(note_id=note).values)
    return JsonResponse({'Text for user {who}  is : ', qs__note})

