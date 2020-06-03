# Generated by Django 2.2.12 on 2020-05-13 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userdata', '0002_auto_20200513_1658'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lenguaje', models.CharField(max_length=255, null=True, verbose_name='Lenguajes')),
                ('MotorDB', models.CharField(max_length=255, null=True, verbose_name='Motor de base de datos')),
                ('Arquitectura', models.CharField(max_length=255, null=True, verbose_name='Arquitectura')),
            ],
            options={
                'verbose_name': 'Categoria del proyecto',
                'verbose_name_plural': 'Categorias de los proyectos',
            },
        ),
        migrations.CreateModel(
            name='TipoDocu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreTipoDocu', models.CharField(default='Documento', max_length=255, verbose_name='Nombre tipo documento')),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreProy', models.CharField(max_length=255, null=True, verbose_name='Nombre del proyecto')),
                ('DescProy', models.CharField(max_length=255, null=True, verbose_name='Descipcion del proyecto')),
                ('ImgProy', models.ImageField(default='proyecto.png', upload_to='imgProyecto/', verbose_name='Imagen del proyecto')),
                ('FechaInio', models.DateField(auto_now_add=True, null=True, verbose_name='Fecha de inicio del proyecto')),
                ('FechaFin', models.DateField(null=True, verbose_name='Fecha del fin del proyecto ')),
                ('UrlRepo', models.CharField(max_length=255, null=True, verbose_name='Url del repositorio del proyecto')),
                ('EstadoProy', models.CharField(default='en desarrollo', max_length=255, verbose_name='Estado del proyecto')),
                ('idCategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.CategoriaProyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreDocu', models.CharField(max_length=255, null=True, verbose_name='Nombre del proyecto')),
                ('PathDocu', models.CharField(max_length=255, null=True, verbose_name='Direccion del documento')),
                ('idProyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Proyecto', verbose_name='Id del proyecto')),
                ('idTipoDocu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.TipoDocu', verbose_name='Id Tipo de documento')),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userdata.DatosUser', verbose_name='Id del usuario ')),
            ],
        ),
    ]