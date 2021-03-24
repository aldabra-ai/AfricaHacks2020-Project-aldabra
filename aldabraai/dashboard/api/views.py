from rest_framework.decorators import api_view

from appointment.models import (
    Appointment,
)

@api_view(http_method_names=['POST'])
def dashboard(request, **kwargs):
    pass