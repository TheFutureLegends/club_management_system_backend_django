from django.urls import path, include
from . import views
from rest_framework import routers

member_router = routers.DefaultRouter()
member_router.register('members', views.MemberView)
event_router = routers.DefaultRouter()
event_router.register('events', views.EventView)
kpi_router = routers.DefaultRouter()
kpi_router.register('kpis', views.KPIView)

urlpatterns = [
    path('', include(member_router.urls)),
    path('', include(event_router.urls)),
    path('', include(kpi_router.urls))

]
