## REST FRAMEWORK IMPORTS
# from rest_framework import (
#     viewsets,
#     generics,
#     status
#     )
#from rest_framework.generics import mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view, #action

## COMMON
#from django.shortcuts import get_object_or_404, redirect
from django.utils.text import slugify


## PATIENT MODELS
from ..models import (
    #Patient, 
    #PatientInsurranceDetail, 
    #PatientBankDetail, 
    PatientReview, 

    #### Doctor Models ####

    Doctor, 
    #DoctorQualification,
    #DoctorSpecialization
)

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





@api_view(http_method_names=['POST'])
def review_doctor(request, slug):
    doctor = Doctor.objects.get(slug=slug)
    if request.method == 'POST':
        serializer = DoctorReviewSerializer(data=request.data)
        review = PatientReview
        if serializer.is_valid():
            review.review_name = serializer.validated_data['review_name']
            review.anonymous_review = serializer.validated_data['anonymous_review']
            review.wait_time_rating = serializer.validated_data['wait_time_rating']
            review.bedside_manner_rating = serializer.validated_data['bedside_manner_rating']
            review.overall_rating = serializer.validated_data['overall_rating']
            review.review = serializer.validated_data['review']
            review.is_doctor_recommended = serializer.validated_data['is_doctor_recommended']
            review.not_recommended_reason = serializer.validated_data['not_recommended_reason']#
            review.publish = serializer.validated_data['publish']
            slug = slugify(review.review_name, allow_unicode=True)

            if serializer.validated_data['publish']:
                serializer.save(owner=request.user, reviewed_doctor=doctor, review_state='PUB', slug=slug)
            else:
                serializer.save(owner=request.user, reviewed_doctor=doctor, review_state='DFT', slug=slug)
    return Response(serializer.data)