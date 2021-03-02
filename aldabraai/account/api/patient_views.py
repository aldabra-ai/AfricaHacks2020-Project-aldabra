## MODELS
from ..models import Patient, PatientInsurranceDetail, PatientBankDetail, PatientReview
## SERIALIZERS
from .patient_serializers import PatientDetailSerializer,PatientBankDetailSerializer,PatientInsurranceDetailSerializer,PatientReviewSerializer
## REST FRAMEWORK IMPORTS
from rest_framework import serializers, viewsets
from rest_framework.generics import mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
## COMMON
from django.shortcuts import get_object_or_404, redirect


class CreateUpdateRetrieveViewset(mixins.CreateModelMixin,
                                  mixins.RetrieveModelMixin,
                                  mixins.UpdateModelMixin,
                                  viewsets.GenericViewSet):
        pass


class PatientProfileAPIView(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientDetailSerializer
    lookup_field = 'slug'

    def create(self, *args, **kwargs):
        response = super(PatientProfileAPIView, self).create(*args, **kwargs)
        #return redirect('accounts:set-profile-slug')
        return Response(response.data, )

    def perform_create(self, serializer):
        user = self.request.user
        username = user.identifier
        full_name = user.full_name
        serializer.save(owner=user, full_name=full_name, slug=username)


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

class PatientIsurranceDetailAPI(CreateUpdateRetrieveViewset):
    queryset = PatientInsurranceDetail.objects.all()
    serializer_class = PatientInsurranceDetailSerializer
    lookup_field = 'patient'

    def list(self, request):
        queryset = self.get_queryset()
        serializer = PatientInsurranceDetailSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, patient):
        queryset = self.get_queryset()
        username = request.user.identifier
        serializer = PatientInsurranceDetailSerializer()
        if patient == username:
            details = get_object_or_404(queryset, patient=request.user)
            serializer = PatientInsurranceDetailSerializer(details)
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_401_UNAUTHORIZED)

    def create(self, request, *args, **kwargs):
        response = super(PatientIsurranceDetailAPI, self).create(request, *args, **kwargs)
        
        return Response(response.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        user = self.request.user
        bank_details = get_object_or_404(PatientBankDetail, patient=user)
        serializer.save(patient=user, bank_details=bank_details)

class PatientReviewAPI(viewsets.ModelViewSet):
    queryset = PatientReview.objects.all()
    serializer_class = PatientReviewSerializer
    multiple_lookup_fields = ['patient', 'pk']

    def create(self, request, *args, **kwargs):
        response = super(PatientReviewAPI, self).create(request, *args, **kwargs)

        return Response(response.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        user = self.request.user
        
        if serializer.validated_data['publish']:
            serializer.save(patient=user, review_state='PUB')
        else:
            serializer.save(patient=user)
        
    def get_object(self):
        queryset = self.get_queryset()
        filter = {}
        fields = self.multiple_lookup_fields
        for field in fields:
            filter[field] = self.kwargs[field]

        review = get_object_or_404(queryset, **filter)
        return review
