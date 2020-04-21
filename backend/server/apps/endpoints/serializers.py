'''
So far we have defined database models, but we will not see anything new when running the web server.
We need to specify REST API to our objects. The simplest and cleanest way to achieve this is to use Django REST Framework (DRF).
To install DRF we need to run: -->
    pip3 install djangorestframework
    pip3 install markdown       # Markdown support for the browsable API.
    pip3 install django-filter  # Filtering support
and add it to INSTALLED_APPS in backend/server/server/settings.py: --> 'rest_framework', # add django rest framework

--------> ----------> To see something in the browser we need to define:

    A - serializers - they will define how database objects are mapped in requests,
    B - views - how our models are accessed in REST API,
    C - urls - definition of REST API URL addresses for our models.
'''

'''
Let's start with the DRF Serializers
Please add serializers.py file to server/apps/endpoints directory:
'''

# backend/server/apps/endpoints/serializers.py file
from rest_framework import serializers
from apps.endpoints.models import Endpoint
from apps.endpoints.models import MLAlgorithm
from apps.endpoints.models import MLAlgorithmStatus
from apps.endpoints.models import MLRequest


class EndpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endpoint
        read_only_fields = ("id", "name", "owner", "created_at")
        fields = read_only_fields


class MLAlgorithmSerializer(serializers.ModelSerializer):
    current_status = serializers.SerializerMethodField(read_only=True)

    def get_current_status(self, mlalgorithm):
        return MLAlgorithmStatus.objects.filter(parent_mlalgorithm=mlalgorithm).latest('created_at').status

    class Meta:
        model = MLAlgorithm
        read_only_fields = ("id", "name", "description", "code",
                            "version", "owner", "created_at",
                            "parent_endpoint", "current_status")
        fields = read_only_fields


class MLAlgorithmStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLAlgorithmStatus
        read_only_fields = ("id", "active")
        fields = ("id", "active", "status", "created_by", "created_at",
                  "parent_mlalgorithm")


class MLRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLRequest
        read_only_fields = (
            "id",
            "input_data",
            "full_response",
            "response",
            "created_at",
            "parent_mlalgorithm",
        )
        fields = (
            "id",
            "input_data",
            "full_response",
            "response",
            "feedback",
            "created_at",
            "parent_mlalgorithm",
        )


'''
Serializers will help with packing and unpacking database objects into JSON objects. 
In Endpoints and MLAlgorithm serializers, we defined all read-only fields. This is because, 
we will create and modify our objects only on the server-side.For MLAlgorithmStatus, fields status, created_by, 
created_at and parent_mlalgorithm are in read and write mode, we will use the to set algorithm status by REST API. 
For MLRequest serializer there is a feedback field that is left in read and write mode - it will be needed to provide
feedback about predictions to the server.

The MLAlgorithmSerializer is more complex than others. It has one filed current_status that represents the latest status
from MLAlgorithmStatus.
'''