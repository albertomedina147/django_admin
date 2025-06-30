from django.contrib import admin
from .models import Curso # Importa tu modelo Curso

# Define la clase personalizada para el administrador de Curso
class CursoAdmin(admin.ModelAdmin):
    # 1. Dar formato a la tabla donde se visualizan los cursos registrados
    # Elige los campos que deseas mostrar en la lista de cursos
    list_display = (
        'nombre',
        'nivel',
        'precio',
        'duracion_horas',
        'disponible',
        'fecha_creacion',
        'ultima_actualizacion'
    )

    # 2. Agrega una barra de búsqueda
    # Permite buscar por nombre y descripción del curso
    search_fields = (
        'nombre',
        'descripcion',
        'idioma' # También se puede buscar por idioma
    )

    # 3. Agrega una búsqueda por fecha (filtros de fecha)
    # Django automáticamente crea filtros de fecha para campos DateTimeField
    date_hierarchy = 'fecha_creacion'

    # 4. Agrega una barra de filtro lateral
    # Elige los campos por los que deseas filtrar
    list_filter = (
        'nivel',
        'disponible',
        'idioma',
        'fecha_creacion' # Permite filtrar por año, mes, día
    )

    # 5. Ordenar los datos por fecha de creación de más antigua a más reciente
    # Esto ya está definido en el Meta de tu modelo, pero también se puede forzar aquí
    # ordering = ('fecha_creacion',) # Ya está en el modelo, no es estrictamente necesario aquí

    # 6. Modificar los nombres de los campos que se visualizan en el formulario de registro del administrador
    # Esto se logra en gran medida con 'verbose_name' en el modelo.
    # Aquí puedes agrupar campos y especificar cuáles se muestran/editan.
    fieldsets = (
        ('Información Básica del Curso', {
            'fields': ('nombre', 'descripcion', 'imagen'),
            'description': 'Datos fundamentales para la identificación del curso.'
        }),
        ('Detalles y Características', {
            'fields': ('nivel', 'idioma', 'duracion_horas', 'precio', 'disponible'),
            'classes': ('collapse',), # Esto hace que la sección sea colapsable
            'description': 'Propiedades y configuración del curso.'
        }),
        ('Fechas y Trazabilidad (Automático)', {
            'fields': ('fecha_creacion', 'ultima_actualizacion'),
            'classes': ('wide', 'extrapretty'), # Clases CSS para mejorar la apariencia (opcional)
            'description': 'Campos gestionados automáticamente por el sistema.'
        }),
    )

    # 7. Visualiza los campos automáticos (solo lectura)
    # Asegúrate de que los campos auto_now_add y auto_now sean de solo lectura
    readonly_fields = (
        'fecha_creacion',
        'ultima_actualizacion'
    )


# Registra tu modelo con la clase de administración personalizada
admin.site.register(Curso, CursoAdmin)