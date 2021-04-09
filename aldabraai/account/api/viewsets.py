## REST FRAMEWORK IMPORTS
from django.db.models import query
from rest_framework import ( 
    viewsets,
    generics,
    status
    )
from rest_framework.generics import mixins
from rest_framework.response import Response
from rest_framework.decorators import (
    action, 
    api_view
    )

## COMMON
from django.shortcuts import (
    get_object_or_404, 
    redirect
    )
from django.utils.text import slugify
from ..utils import (
    generate_random_string,
    generate_uuid,
)


## PATIENT MODELS
from ..models import (
    #### PATIENT Models ####
    Patient, 
    PatientInsuranceDetail, 
    PatientBankDetail, 
    PatientReview, 

    #### Doctor Models ####
    Doctor, 
    DoctorQualification,
    DoctorSpecialization
)

## SERIALIZERS
from .serializers import (
    #### PATIENT SERIALIZERS ####
    PatientDetailSerializer,
    PatientBankDetailSerializer,
    PatientInsuranceDetailSerializer,
    DoctorReviewSerializer,

    #### DOCTOR SERIALIZERS ####
    DoctorDetailSerializer, 
    DoctorQualificationSerializer,
    DoctorSpecializationSerializer,
)



class CreateUpdateRetrieveViewset(mixins.CreateModelMixin,
                                  mixins.RetrieveModelMixin,
                                  mixins.UpdateModelMixin,
                                  viewsets.GenericViewSet):
        pass

class ListRetreiveUpdateViewset(mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          viewsets.GenericViewSet):
        pass


############# DOCTOR VIEWSETS ########################################

class DoctorProfileAPIView(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorDetailSerializer
    lookup_field = 'slug'

    def create(self, *args, **kwargs):
        response = super(DoctorProfileAPIView, self).create(*args, **kwargs)
        #return redirect('accounts:set-profile-slug')
        return Response(response.data)

    def perform_create(self, serializer):
        user = self.request.user
        username = slugify(user.identifier)
        full_name = user.full_name
        serializer.save(owner=user, full_name=full_name, slug=username)




class DoctorQualificationAPI(CreateUpdateRetrieveViewset):
    queryset = DoctorQualification.objects.all()
    serializer_class = DoctorQualificationSerializer
    lookup_field = 'pk'


    def retrieve(self, request, pk):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=pk)

        serializer = DoctorQualificationSerializer(obj)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        response = super(DoctorQualificationAPI, self).create(request, *args, **kwargs)

        return Response(response.data)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(doctor=user)




class DoctorSpecializationAPI(CreateUpdateRetrieveViewset):
    queryset = DoctorSpecialization.objects.all()
    serializer_class = DoctorSpecializationSerializer
    lookup_field = 'pk'        

    def retrieve(self, request, pk):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=pk)

        serializer = DoctorSpecializationSerializer(obj)
        return Response(serializer.data)


    def create(self, request, *args, **kwargs):
        response = super(DoctorSpecializationAPI, self).create(request, *args, **kwargs)

        return Response(response.data)


    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(doctor=user)




############### PATIENT VIEWSETS ####################


class PatientProfileAPIView(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientDetailSerializer
    lookup_field = 'slug'

    def create(self, *args, **kwargs):
        response = super(PatientProfileAPIView, self).create(*args, **kwargs)
        #return redirect('accounts:set-profile-slug')
        return Response(response.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        user = self.request.user
        username = user.identifier
        full_name = user.full_name
        serializer.save(
            owner=user, 
            full_name=full_name, 
            slug=username
            )




class PatientBankDetailAPI(CreateUpdateRetrieveViewset):
    queryset = PatientBankDetail.objects.all()
    serializer_class = PatientBankDetailSerializer
    lookup_field = 'patient'

    def list(self, request):
        queryset = self.get_queryset()
        serializer = PatientBankDetailSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, patient):
        queryset = self.get_queryset()
        username = request.user.identifier
        serializer = PatientBankDetailSerializer()
        if patient == username:
            details = get_object_or_404(queryset, patient=request.user)
            serializer = PatientBankDetailSerializer(details)
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_401_UNAUTHORIZED)

    def create(self, request, *args, **kwargs):
        response = super(PatientBankDetailAPI, self).create(request, *args, **kwargs)

        return Response(response.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(patient=user)





class PatientInsuranceDetailAPI(CreateUpdateRetrieveViewset):
    queryset = PatientInsuranceDetail.objects.all()
    serializer_class = PatientInsuranceDetailSerializer
    lookup_field = 'patient'

    def list(self, request):
        queryset = self.get_queryset()
        serializer = PatientInsuranceDetailSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, patient):
        queryset = self.get_queryset()
        username = request.user.identifier
        serializer = PatientInsuranceDetailSerializer()
        if patient == username:
            details = get_object_or_404(queryset, patient=request.user)
            serializer = PatientInsuranceDetailSerializer(details)
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_401_UNAUTHORIZED)

    def create(self, request, *args, **kwargs):
        response = super(PatientInsuranceDetailAPI, self).create(request, *args, **kwargs)
        
        return Response(response.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        user = self.request.user
        bank_details = get_object_or_404(PatientBankDetail, patient=user)
        serializer.save(patient=user, bank_details=bank_details)





class DoctorReviewAPI(ListRetreiveUpdateViewset):
    serializer_class = DoctorReviewSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        user = self.request.user
        reviews = PatientReview.objects.all()
        return reviews

    def list(self, request):
        queryset = self.get_queryset()
        serializer = DoctorReviewSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, slug):
        review = get_object_or_404(PatientReview, slug=slug)
        serializer = DoctorReviewSerializer(instance=review)
        return Response(serializer.data, status=status.HTTP_200_OK)




    

