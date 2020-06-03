from django.db import models
from .genero import Generos
from ckeditor.fields import RichTextField
# Crer la estructura de la app
class Roles(models.Model):
    roleName = models.CharField(max_length=50,verbose_name="Nombre del rol",default="usuario")
    class Meta:
        verbose_name ="perfil de usuario"
        verbose_name_plural="perfiles"
    def __str__(self):
        return self.roleName
class DatosUser(models.Model):
    userDNI = models.CharField(max_length=20,verbose_name="ID de el usuario")
    nombreUser= models.CharField(max_length=255,verbose_name="Nombre",null=True)
    profecionUser = models.CharField(max_length=255, verbose_name="Profecion",null=True)
    fotoUser = models.ImageField(default='user.png', upload_to="imgPerfil/",verbose_name="foto de perfil",null=True)
    telUser = models.CharField(max_length=20,verbose_name="Telefono del usuario",null=True)
    direccion=  models.CharField(max_length=255,verbose_name="direccion de usuario",null=True)
    generoUser = models.CharField(max_length=10,choices=Generos,default="O",verbose_name="Genero",null=True)
    upData = models.DateTimeField(auto_now_add=True,auto_now=False,null=True,verbose_name="creado",)
    modificado = models.DateTimeField(auto_now=True,null=True,verbose_name="modificado",)
    class Meta:
        verbose_name ="dato de usuario"
        verbose_name_plural="Datos de usuarios "
    def __str__(self):
        return self.userDNI
class Habilidades(models.Model):
    nombreHabilidad= models.CharField(max_length=255,verbose_name="Nombre de la habilidad",null=True)
    descipcionHabilidad= models.TextField(max_length=2000,default="Desarrollador",verbose_name="Descripcion de habilidad",null=True)
    class Meta:
        verbose_name ="Habilidades del usuario"
        verbose_name_plural="Habilidades de los usuarios"
    def __str__(self):
        return self.nombreHabilidad
class Rates(models.Model):
    idHabilidades = models.ForeignKey(Habilidades,on_delete=models.CASCADE,verbose_name="Id de la habilidad")
    idUSuario = models.ForeignKey(DatosUser,on_delete=models.CASCADE,verbose_name="Id del usuario",null=True)
    Porcentaje = models.DecimalField(max_digits=2,decimal_places=1,verbose_name="Porcentaje de dominio de la habilidad",default=0.0)
    udtHabilidad=models.DateTimeField(auto_now_add=True,null=True,verbose_name="Fecha de actualizacion de la habilidad")
    class Meta:
        verbose_name ="Nivel de habilidad"
        verbose_name_plural="Niveles de usuarios"
    def __unicode__(self):
        return self.idUSuario
class DetaRoles(models.Model):
    idRoles = models.ForeignKey(Roles, on_delete=models.CASCADE,verbose_name="Id del rol")
    idUsuario = models.ForeignKey(DatosUser,on_delete=models.CASCADE,verbose_name="Id del usuario")
    Agregado = models.DateTimeField(auto_now_add=True,auto_now=False,null=True,verbose_name="Fecha de agregacion del rol")
    addUser = models.DateTimeField(auto_now=True,null=True,verbose_name="Fecha de agregacion de user")
    EstadoRol = models.CharField(max_length=20,verbose_name="Estado del rol",default="activo")
    class Meta:
        verbose_name ="Rol usuario"
        verbose_name_plural="Roles de los usuarios"
    def __unicode__(self):
        return self.idUsuario

