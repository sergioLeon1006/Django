from django.db import models
#from userdata.models  import DatosUser
# Create your models here.
class CategoriaProyecto(models.Model):
    Lenguaje = models.CharField(max_length=255,verbose_name="Lenguajes")
    MotorDB = models.CharField(max_length=255,verbose_name="Motor de base de datos")
    Arquitectura = models.CharField(max_length=255,verbose_name="Arquitectura")
    class Meta:
        verbose_name = "Categoria del proyecto"
        verbose_name_plural = "Categorias de los proyectos"
    def __str__(self):
        return self.Lenguaje,self.MotorDB,self.Arquitectura
class TipoDocu(models.Model):
    NombreTipoDocu=models.CharField(max_length="255",verbose_name="Nombre tipo documento")
    def __str__(self):
        return self.NombreTipoDocu
class Proyecto(models.Model):
    idCategoria =models.ForeignKey(CategoriaProyecto,on_delete=models.CASCADE)
    NombreProy = models.CharField(max_length=255,verbose_name="Nombre del proyecto")
    DescProy = models.CharField(max_length=255,verbose_name="Descipcion del proyecto")
    ImgProy= models.ImageField(default="proyecto.png",verbose_name="Imagen del proyecto")
    FechaInio=models.DateField(auto_now_add=True,auto_now=False,verbose_name="Fecha de inicio del proyecto")
    FechaFin=models.DateField(auto_now=False,verbose_name="Fecha del fin del proyecto ")
    UrlRepo=models.CharField(max_length=255,verbose_name="Url del repositorio del proyecto")
    EstadoProy=models.CharField(max_length=255,verbose_name="Estado del proyecto")
    def __str__(self):
        return self.NombreProy
class Documento(models.Model):
    idTipoDocu = models.ForeignKey(TipoDocu,on_delete=models.CASCADE,verbose_name="Id Tipo de documento")
    idProyecto =models.ForeignKey(Proyecto,on_delete=models.CASCADE,verbose_name="Id del proyecto")
    #idUsuario =models.ForeignKey(DatosUser,on_delete=models.CASCADE,verbose_name="Id del usuario ")
    NombreDocu =models.CharField(max_length=255,verbose_name="Nombre del proyecto")
    PathDocu =models.CharField(max_length=255,verbose_name="Direccion del documento")
    def __str__(self):
        return self.NombreDocu

