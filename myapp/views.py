from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from myapp.models import Doctor, WorkPlace, Specialty
from myapp.serializers import DoctorSerializer, WorkPlaceSerializer, SpecialtySerializer


# Create your views here.

def doctor_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return JsonResponse(serializer.data, safe=False)


def doctor_detail(request, id):
    doctor = Doctor.objects.get(id=id)
    serializer = DoctorSerializer(doctor)
    return JsonResponse(serializer.data, safe=False)


class WorkPlaceViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = WorkPlace.objects.all()
        serializer = WorkPlaceSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def retrieve(self, request, pk=None):
        queryset = WorkPlace.objects.all()
        workplace = get_object_or_404(queryset, pk=pk)
        serializer = WorkPlaceSerializer(workplace)
        return JsonResponse(serializer.data, safe=False)


class SpecialtyViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Specialty.objects.all()
        serializer = SpecialtySerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def retrieve(self, request, pk=None):
        queryset = Specialty.objects.all()
        specialty = get_object_or_404(queryset, pk=pk)
        serializer = SpecialtySerializer(specialty)
        return JsonResponse(serializer.data, safe=False)

