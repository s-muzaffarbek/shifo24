from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from myapp.models import Doctor, WorkPlace, Specialty
from myapp.serializers import DoctorSerializer, WorkPlaceSerializer, SpecialtySerializer


# Create your views here.

class DoctorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

class WorkPlaceViewSet(viewsets.ModelViewSet):
    queryset = WorkPlace.objects.all()
    serializer_class = WorkPlaceSerializer
    permission_classes = [IsAuthenticated]


class SpecialtyViewSet(viewsets.ModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    permission_classes = [IsAuthenticated]
