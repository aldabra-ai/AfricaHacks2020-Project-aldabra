## REST FRAMEWORK IMPORTS
# from rest_framework import (
#     viewsets,
#     generics,
#     status
#     )
#from rest_framework.generics import mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import (
    api_view, 
    #action
)

from rest_framework.generics import CreateAPIView, get_object_or_404

## COMMON
#from django.shortcuts import get_object_or_404, redirect
from django.utils.text import slugify
from ..utils import (
    generate_random_string,
    #generate_uuid
)

## PATIENT MODELS
from ..models import (
    #Patient, 
    #PatientInsurranceDetail, 
    #PatientBankDetail, 
    #PatientReview, 

    #### Doctor Models ####

    Doctor, 
    #DoctorQualification,
    #DoctorSpecialization
)

from authend.models import User

## SERIALIZERS
from .serializers import (
    #### DOCTOR SERIALIZERS ####
    #DoctorDetailSerializer, 
    #DoctorQualificationSerializer,
    #DoctorSpecializationSerializer,

    #### PATIENT SERIALIZERS ####
    #PatientDetailSerializer,
    #PatientBankDetailSerializer,
    #PatientInsurranceDetailSerializer,
    DoctorReviewSerializer
)






class ReviewDoctorAPI(CreateAPIView):
    '''
    
    '''

    serializer_class = DoctorReviewSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        
        return Response(response.data, status=status.HTTP_201_CREATED)

    def perfome_create(self, serializer):
        doctor = get_object_or_404(Doctor, slug=self.kwargs['slug'])
        review_name = serializer.data['review_name']
        rand_string = generate_random_string()
        slug = slugify(f'{review_name + rand_string}')

        if serializer.data['publish']:
            serializer.save(
                owner=self.request.user, 
                reviewed_doctor=doctor,
                review_state='PUB',
                slug=slug
                )
        else:
            serializer.save(
                owner=self.request.user, 
                reviewed_doctor=doctor,
                review_state='DFT',
                slug=slug
                )

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)