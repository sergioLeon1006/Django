from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.urls import reverse
# Create your views here.
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