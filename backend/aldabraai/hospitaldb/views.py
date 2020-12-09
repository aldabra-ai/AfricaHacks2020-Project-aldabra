from rest_framework import status
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .models import Appointment,Speciality,Doctor,Nurse,Hospital,Room,Block
from .serializer import HospitalSerializer,AppointmentSerializer,DoctorSerializer,SpecialitySerializer,NurseSerializer,RoomSerializer,BlockSerializer
from rest_framework import generics

class HospitalList(APIView):
    """
    List All Hospitals
    """
    def get(self, request, format=None):
        hospitals = Hospital.objects.all()
        serializer = HospitalSerializer(hospitals, context={'request': request},many=True)
        return Response(serializer.data)

    def post(sefl, request, format=None):
        serializer = HospitalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HospitalDetail(APIView):
    """
    Retrieve, update or delete a hospital instance.
    """

    def get_object(self, pk):
        try:
            return Hospital.objects.get(pk=pk)
        except Hospital.DoesNotExist:
            raise Http404

    def get(self, rquest, pk, format=None):
        hospital = self.get_object(pk)
        serializer = HospitalSerializer(hospital)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        hospital = self.get_object(pk)
        serializer = HospitalSerializer(hospital, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class DoctorList(APIView):
    """
    Retrieve Doctor List
    """

    def get(self, request, format=None):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, context={'request': request},many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoctorDetail(APIView):

    def get_object(self, pk):
        try:
            return Doctor.objects.get(pk=pk)
        except Doctor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        doctor = self.get_object(pk)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        doctor = self.get_object(pk)
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NurseList(generics.ListCreateAPIView):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer

class NurseDetail(generics.RetrieveUpdateAPIView):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer

class AppointmentList(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentDetail(generics.RetrieveDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    
class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomDetail(generics.RetrieveUpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class BlockList(generics.ListCreateAPIView):
    queryset = Block.objects.all()
    serializer_class = RoomSerializer

class BlockDetail(generics.RetrieveUpdateAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer


