from django.shortcuts import render
from rest_framework import viewsets

# Import member's model and serializer

from .models import Member, Event, KPI
from .serializers import MemberSerializer, EventSerializer, KPISerializer


# Create your views here.

class MemberView(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class EventView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class KPIView(viewsets.ModelViewSet):
    queryset = KPI.objects.all()
    serializer_class = KPISerializer
