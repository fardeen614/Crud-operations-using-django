

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def baba(request):
    return HttpResponse("beta")
def tull(request):

    return HttpResponse("aaja")
def meragame(request):

    if request.method == "POST":

     data_taken = request.POST
     print(data_taken)
     music_nme = data_taken.get('mus1')
     music_decription = data_taken.get('mus2')
     music_imge = request.FILES.get('mus3')

     print(music_decription)
     print(music_nme)
     print(music_imge)
     Music.objects.create(music_name=music_nme,music_description=music_decription,music_image=music_imge)
     return redirect('/meragame')
    query_set = Music.objects.all()




    return render(request,"amtu.html",context = {'rapun':query_set})
def deleteval(request,id):
    option_todelete = Music.objects.get(id = id)
    option_todelete.delete()

    return redirect('/meragame')

def updateval(request,id):
    babes= Music.objects.get(id=id)

    if request.method == "POST":

     data_taken = request.POST
     print(data_taken)
     music_nme = data_taken.get('mus1')
     music_decription = data_taken.get('mus2')
     music_imge = request.FILES.get('mus3')
     print(music_decription)
     print(music_nme)
     print(music_imge)
     babes.music_name = music_nme
     babes.music_description = music_decription
     if music_imge:
         babes.music_image = music_imge


     babes.save()
     return redirect('/meragame')
    context={'receipe':babes}











    return render(request,"update.html",context)







