from django.db import models
from django.utils import timezone

class Curso(models.Model):
    # Tipos de datos adicionales (5 tipos diferentes)
    NIVEL_CHOICES = [
        ('Basico', 'Básico'),
        ('Intermedio', 'Intermedio'),
        ('Avanzado', 'Avanzado'),
    ]

    nombre = models.CharField(
        max_length=200,
        verbose_name="Título del Curso" # Nombre amigable para el administrador
    )
    descripcion = models.TextField(
        verbose_name="Descripción Detallada"
    )
    precio = models.DecimalField( # Tipo 1: DecimalField
        max_digits=10,
        decimal_places=2,
        verbose_name="Precio (USD)"
    )
    duracion_horas = models.IntegerField( # Tipo 2: IntegerField
        verbose_name="Duración (horas)"
    )
    disponible = models.BooleanField( # Tipo 3: BooleanField
        default=True,
        verbose_name="¿Disponible para Inscripción?"
    )
    nivel = models.CharField( # Tipo 4: CharField con opciones
        max_length=20,
        choices=NIVEL_CHOICES,
        default='Basico',
        verbose_name="Nivel de Dificultad"
    )
    idioma = models.CharField( # Tipo 5: CharField
        max_length=50,
        default='Español',
        verbose_name="Idioma del Curso"
    )

    # Campos requeridos (imagen y fecha de creación)
    imagen = models.ImageField(
        upload_to='cursos_imagenes/', # Las imágenes se guardarán en media/cursos_imagenes/
        blank=True,
        null=True,
        verbose_name="Miniatura del Curso"
    )
    fecha_creacion = models.DateTimeField(
        auto_now_add=True, # Se establece automáticamente la fecha y hora cuando se crea el objeto
        verbose_name="Fecha de Creación"
    )
    ultima_actualizacion = models.DateTimeField(
        auto_now=True, # Se actualiza automáticamente cada vez que se guarda el objeto
        verbose_name="Última Actualización"
    )

    class Meta:
        # Ordenar los datos por fecha de creación (de más antigua a más reciente)
        # El guion (-) sería para ordenar de más reciente a más antigua
        ordering = ['fecha_creacion']
        # Nombre de la lista en el panel de administrador
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.nombre
