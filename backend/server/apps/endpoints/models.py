'''
#Build Django models to store information about ML algorithms and requests in the database,
#Create Django models
#To create Django models we need to create a new app --->
'''
'''
    # run this in backend/server directory
    python manage.py startapp endpoints
    mkdir apps
    mv endpoints/ apps/
    With the above commands, we have created the endpoints app and moved it to the apps directory.
    I have added the apps directory to keep the project clean.

    # list files in apps/endpoints
    ls apps/endpoints/
    # admin.py  apps.py  __init__.py  migrations  models.py  tests.py  views.py
    Let's go to apps/endpoints/models.py file and define database models (Django provides object-relational mapping layer (ORM)).
    and start defining our classes which will store data about the ML Algorithm & the Requests in DB.
'''

from django.db import models

# Create your models here.

class Endpoint(models.Model):
    '''
    The Endpoint object represents ML API endpoint.

    Attributes:
        name: The name of the endpoint, it will be used in API URL,
        owner: The string with owner name,
        created_at: The date when endpoint was created.
    '''
    name = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now=True ,blank=True)

class MLAlgorithm(models.Model):
    '''
    The MLAlgorithm represent the ML algorithm object.

    Attributes:
        name: The name of the algorithm.
        description: The short description of how the algorithm works.
        code: The code of the algorithm.
        version: The version of the algorithm similar to software versioning.
        owner: The name of the owner.
        created_at: The date when MLAlgorithm was added.
        parent_endpoint: The reference to the Endpoint.
    '''
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1000)
    code = models.CharField(max_length=50000)
    version = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)

class MLAlgorithmStatus(models.Model):
    '''
    The MLAlgorithmStatus represent status of the MLAlgorithm which can change during the time.

    Attributes:
        status: The status of algorithm in the endpoint. Can be: testing, staging, production, ab_testing.
        active: The boolean flag which point to currently active status.
        created_by: The name of creator.
        created_at: The date of status creation.
        parent_mlalgorithm: The reference to corresponding MLAlgorithm.

    '''
    status = models.CharField(max_length=128)
    active = models.BooleanField()
    created_by = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE, related_name = "status")

class MLRequest(models.Model):
    '''
    The MLRequest will keep information about all requests to ML algorithms.

    Attributes:
        input_data: The input data to ML algorithm in JSON format.
        full_response: The response of the ML algorithm.
        response: The response of the ML algorithm in JSON format.
        feedback: The feedback about the response in JSON format.
        created_at: The date when request was created.
        parent_mlalgorithm: The reference to MLAlgorithm used to compute response.
    '''
    input_data = models.CharField(max_length=100000)
    full_response = models.CharField(max_length=100000)
    response = models.CharField(max_length=100000)
    feedback = models.CharField(max_length=100000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE)

'''
Until Now : 
We defined three models:

    A - Endpoint - to keep information about our endpoints,
    B - MLAlgorithm - to keep information about ML algorithms used in the service,
    C - MLAlgorithmStatus - to keep information about ML algorithm statuses. The status can change in time, 
        for example, we can set testing as initial status and then after testing period switch to production state.
    D - MLRequest - to keep information about all requests to ML algorithms. It will be needed to monitor ML algorithms 
        and run A/B tests.

Now --> We need to add our app to INSTALLED_APPS in backend/server/server/settings.py, it should look like:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # apps
    'apps.endpoints'
    
After Adding our App --> to Our installed Apps

Now --> We need To apply our models to the database, Therefore --> we need to run migrations:
    # please run it in backend/server directory
            $ python manage.py makemigrations
            $python manage.py migrate
            
    The above commands will create tables in the database. By default, 
    Django is using SQLite as a database. For this tutorial, 
    we can keep this simple database, for more advanced projects you can set a Postgres or MySQL as a database 
    (you can configure this by setting DATABASES variable in backend/server/server/settings.py).
]
'''