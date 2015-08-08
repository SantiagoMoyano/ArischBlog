from django.shortcuts import render
from blog.models import Entrada, Categoria, Contacto, Mensajes
from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    context = RequestContext(request)
    post = Entrada.objects.filter(published = True)
    return render_to_response('blog.html', {'posts':post}, context)

def ver_post(request, id_post):
    context = RequestContext(request)
    mi_post = Entrada.objects.get(id=id_post)
    return render_to_response('post.html', 
                              {'post':mi_post},
                              context)

def save_message(request):
    context = RequestContext(request)
    mensajes = None
    if request.method == 'POST':
        mi_post = Entrada.objects.get(id=request.POST['id'])
        nombre= request.POST['nombre']
        mensaje= request.POST['mensaje']        
        msje = Mensajes()
        msje.nombre = nombre
        msje.mensaje = mensaje
        msje.published_in = mi_post
        msje.save()
        mensajes = Mensajes.objects.filter(published_in=mi_post, published = True)

        return render_to_response('mensajes.html', 
                                  {'mensajes':mensajes},
                                  context)

def cont(request):
    context  = RequestContext(request)
    import os
    if request.method=="POST":
        os.system("zenity --info --text \""+"PATO"+"\"")

        nombre = request.POST["nombre"]
        mail = request.POST['mail']
        #asunto = request.POST['asunto']
        mensaje = request.POST["mensaje"]
        contacto = Contacto()
        contacto.nombre = nombre
        contacto.mail = mail
        #contacto.asunto= asunto
        contacto.mensaje = mensaje
        contacto.save()
        mensaje = 'Hey! '+nombre+' te hablo desde '+mail+' para hablar sobre . \n'+mensaje
        from_email = settings.EMAIL_HOST_USER
        send_mail('asunto', mensaje, from_email, [mail], fail_silently=False)
    return render_to_response("cont.html",
                             context)

def dr(request):
    return render_to_response('dr.html')

def ejs(request):
    return render_to_response('ejs.html')

def calc(request):
    return render_to_response('calc.html')

def conv(request):
    return render_to_response('conv.html')

def cron(request):
    return render_to_response('cron.html')

def load(request):
    return render_to_response('load.html')

def troll(request):
    return render_to_response('troll.html')

def trolling(request):
    return render_to_response('trolling.html')
