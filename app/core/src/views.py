from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.views.generic.base import TemplateView
from .forms import Contacto
from django.core.mail import EmailMessage
# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,{
            'tituloIni':'Sobre SAV','titulo2':'clases', 'sobre':'SAV será un aplicativo web dirigido al área de contrato de aprendizaje del SENA, este ayudará a los trabajadores de esta área a organizar una base de datos con información de aprendices que cuentan o no con una alternativa para la etapa productiva; con este aplicativo se podrá ver la información en conjunto como programa de Formación y/o ficha como también la información de un aprendiz en particular lo que brindará un apoyo más rápido y eficaz para la búsqueda de tal información a los usuarios.',
            'funcion':'Permitir administrar la información y la gestión documental pertinente a los procesos de seguimiento de alternativas al Contrato de Aprendizaje, tanto en la fase lectiva como en la fase productiva.',
         })
class NosotrosPageView(TemplateView):
    template_name = "nosotros.html"
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,{
            'profecion2': 'Back developer',
            'profecion': 'Web Designer',
            'user3': 'Denisse Alejandra',
            'user2': 'Sergio León',
            'user1': 'Laura Vanessa',
            'about': 'Estudiantes bien pros de ADSI (tecnologia en anasis y desallo de sistemas de informacion.)',
        })
def ContactoPageView(request):
    formContac =Contacto()
    #validacion
    if request.method == "POST":
        formContac=Contacto(data=request.POST)
        if formContac.is_valid():
            tipomensaje= request.POST.get('tipomensaje','')
            usuario= request.POST.get('usuario','')
            correo= request.POST.get('correo','')
            mensaje= request.POST.get('mensaje','')
            #enviar mensaje jeje :3
            email = EmailMessage(
                "RepoDeveluper: tines un nuevo mensaje",
                "De {} <{}>\n\nEscribio:\n{}\ntipo mensaje {}".format(usuario,correo,mensaje,tipomensaje),
                "no-contestar@inbox.mailtrap.io",
                ["sergiosaldarriagadavila@gmail.com"],
                reply_to=[correo]
            )
            #enviar correo
            try:
                email.send()
                return redirect(reverse('contacto') + "?ok")
            except:
                #no se envió
                return redirect(reverse('contacto')+"?fail")
    return render(request, 'contacto.html',{'formulario':formContac})