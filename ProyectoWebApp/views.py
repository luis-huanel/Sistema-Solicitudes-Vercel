from django.shortcuts import render, redirect, get_object_or_404
from autenticacion.models import Usuario_Registro
from solicitudes.models import Solicitudes_Epps, Solicitudes_Retiro, Solicitudes_Tolva
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver


from django.utils import timezone
from datetime import timedelta


from django.shortcuts import render
from django_user_agents.utils import get_user_agent


# Vista del index, mostrando usuarios conectados
def index(request):
    user_agent = get_user_agent(request)

    # Comprobar si el dispositivo es móvil
    if user_agent.is_mobile:
        # Redirigir a una página de advertencia o mostrar un mensaje
        return render(request, 'ProyectoWebApp/bloqueado.html')  # Asegúrate de tener este template

    usuarios_conectados = Usuario_Registro.objects.filter(is_online=True)  # Obtén los usuarios en línea
    context = {
        'usuarios_conectados': usuarios_conectados
    }
    return render(request, 'ProyectoWebApp/index.html', context)
# Vista para redirigir al panel de administración de Django
@login_required
def admin_panel(request):
    return redirect(reverse('admin:index'))


@login_required
def panel_administrativo_operacional(request):
    # Obtener todas las solicitudes de cada tipo
    solicitudes_epps = Solicitudes_Epps.objects.all()
    solicitudes_retiro = Solicitudes_Retiro.objects.all()
    solicitudes_tolva = Solicitudes_Tolva.objects.all()

    # Ver cambios recientes (últimos 7 días, por ejemplo)
    una_semana_atras = timezone.now() - timedelta(days=7)
    solicitudes_epps_recientes = Solicitudes_Epps.objects.filter(updated__gte=una_semana_atras)
    solicitudes_retiro_recientes = Solicitudes_Retiro.objects.filter(updated__gte=una_semana_atras)
    solicitudes_tolva_recientes = Solicitudes_Tolva.objects.filter(updated__gte=una_semana_atras)

    # Renderizar la plantilla con todas las solicitudes y sus filtros
    return render(request, "ProyectoWebApp/panel_administrativo_operacional.html", {
        "solicitudes_epps": solicitudes_epps,
        "solicitudes_retiro": solicitudes_retiro,
        "solicitudes_tolva": solicitudes_tolva,
        "solicitudes_epps_recientes": solicitudes_epps_recientes,
        "solicitudes_retiro_recientes": solicitudes_retiro_recientes,
        "solicitudes_tolva_recientes": solicitudes_tolva_recientes,
    })

# Vista del panel de trabajador con solicitudes filtradas por el usuario
@login_required
def panel_trabajador(request):
    solicitudes_epps = Solicitudes_Epps.objects.filter(id_usuario=request.user)
    solicitudes_retiro = Solicitudes_Retiro.objects.filter(id_usuario=request.user)
    solicitudes_tolva = Solicitudes_Tolva.objects.filter(id_usuario=request.user)

    # Renderizar la plantilla con las solicitudes
    return render(request, "ProyectoWebApp/panel_trabajador.html", {
        "solicitudes_epps": solicitudes_epps,
        "solicitudes_retiro": solicitudes_retiro,
        "solicitudes_tolva": solicitudes_tolva
    })

@login_required
def panel_jefe(request):
    # Verificar que el usuario sea un jefe
    if request.user.tipo_usuario != Usuario_Registro.TIPO_USUARIO_JEFE:
        return redirect('index')  # Redirige a una página segura si no es un jefe

    # Obtener las solicitudes propias
    solicitudes_epps_propias = Solicitudes_Epps.objects.filter(id_usuario=request.user)
    solicitudes_retiro_propias = Solicitudes_Retiro.objects.filter(id_usuario=request.user)
    solicitudes_tolva_propias = Solicitudes_Tolva.objects.filter(id_usuario=request.user)

    # Obtener las solicitudes de trabajadores
    trabajadores = Usuario_Registro.objects.filter(tipo_usuario=Usuario_Registro.TIPO_USUARIO_TRABAJADOR)
    solicitudes_epps_trabajadores = Solicitudes_Epps.objects.filter(id_usuario__in=trabajadores)
    solicitudes_retiro_trabajadores = Solicitudes_Retiro.objects.filter(id_usuario__in=trabajadores)
    solicitudes_tolva_trabajadores = Solicitudes_Tolva.objects.filter(id_usuario__in=trabajadores)

    # Combinar ambas consultas
    solicitudes_epps = solicitudes_epps_propias.union(solicitudes_epps_trabajadores)
    solicitudes_retiro = solicitudes_retiro_propias.union(solicitudes_retiro_trabajadores)
    solicitudes_tolva = solicitudes_tolva_propias.union(solicitudes_tolva_trabajadores)

    # Renderizar la plantilla con las solicitudes
    return render(request, "ProyectoWebApp/panel_jefe.html", {
        "solicitudes_epps": solicitudes_epps,
        "solicitudes_retiro": solicitudes_retiro,
        "solicitudes_tolva": solicitudes_tolva,
    })


# Vista del panel del jefe, con acceso a todas las solicitudes
#@login_required
#def panel_jefe(request):
    #solicitudes_epps = Solicitudes_Epps.objects.filter(id_usuario=request.user)
    #solicitudes_retiro = Solicitudes_Retiro.objects.filter(id_usuario=request.user)
    #solicitudes_tolva = Solicitudes_Tolva.objects.filter(id_usuario=request.user)

    # Renderizar la plantilla con las solicitudes
    #return render(request, "ProyectoWebApp/panel_jefe.html", {
        #"solicitudes_epps": solicitudes_epps,
        #"solicitudes_retiro": solicitudes_retiro,
        #"solicitudes_tolva": solicitudes_tolva
    #})

# Señales para manejar usuarios conectados y desconectados
@receiver(user_logged_in)
def set_user_online(sender, request, user, **kwargs):
    user.is_online = True
    user.save()

@receiver(user_logged_out)
def set_user_offline(sender, request, user, **kwargs):
    user.is_online = False
    user.save()
