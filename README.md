# Django_ML_WebService

In this tutorial, We will use Adult Income data set. In this data set, the ML will be used to predict whether income exceeds $50K/year based on census data. All of this will be deployed inside Django Web Service.


### To Test the project on your local machine please follow these steps:
  1. - Download The Repo
  2. - Install needed packages:
        $ pip install requirements.txt 
  3. - You can create your own ML Model in the research directory or you can use mine just for now.
      N.B  You will need to dump both any preprocessing steps + the trained model
  4. - Since the project is previously defined with some models and versions you will need to clear up the DB and start from scratch.
        Delete the db.sqlite3 file from backend/server dir
        Then run the following commands to create a new DB file in the backend/server:
          $ python manage.py makemigrations
          $ python manage.py migrate
  5. - Now run the project using this command at backend/server:
          $ python manage.py runserver
      Then open http://127.0.0.1:8000/api/v1/ or http://localhost:8000/api/v1/ 
      You should be able to see the root dir of the API --> 
      You can check the endpoints and ML algorithms in the browser --> At the URL: 
      http://127.0.0.1:8000/api/v1/endpoints For endpoints, 
      http://127.0.0.1:8000/api/v1/mlalgorithms For algorithms.
  6. - Impportant Notes: Untill this point you have the following items working and well defined:
        - A trained ML Aglorithm producing both Preprocessing_Steps & Model as dump(joblib files in /research dir)
        - A Django Project having these capabilites (in backend/server dir):
        
            - models to store information about ML algorithms and requests in the database.
                  Endpoint - to keep information about our endpoints,
                  MLAlgorithm - to keep information about ML algorithms used in the service,
                  MLAlgorithmStatus - to keep information about ML algorithm statuses. The status can change in time, for example, we                                         can set testing as initial status and then after testing period switch to production state.
                  MLRequest - to keep information about all requests to ML algorithms. It will be needed to monitor ML algorithms.
                  
            - a REST API for your ML algorithms with the Django REST Framework which has the following componenets:
                serializers - they will define how database objects are mapped in requests,
                views - how our models are accessed in REST API,
                urls - definition of REST API URL addresses for our models.
                
            - A Specially created App for ML under backend/server/apps/income_classifier which has the ML algorithm code for the SERVER               Side.
            
            - Algorithm Registry : We have the ML code ready and tested. We need to connect it with the server code. 
              a previously created ML Registry object that will keep information about available algorithms and corresponding endpoints.
             
             - A Prediction Service that can accept POST requests with JSON data and forward it to the correct ML algorithm.
    7. - To Test Predictions using Post Requests:         
             - Navigate to backend/server and run the following command in the terminal:
                $ python manage.py runserver
             - Go to http://127.0.0.1:8000/api/v1/income_classifier/predict 
                Then write your JSON Request in correct format Then click POST --> Example:
               

               
                    {"age": 37,
                    "workclass": "Private",
                    "fnlwgt": 34146,
                    "education": "HS-grad",
                    "education-num": 9,
                    "marital-status": "Married-civ-spouse",
                    "occupation": "Craft-repair",
                    "relationship": "Husband",
                    "race": "White",
                    "sex": "Male",
                    "capital-gain": 0,
                    "capital-loss": 0,
                    "hours-per-week": 68,
                    "native-country": "United-States"}
                    

                
          - you should be able to see the ML Algorithm Response like with estimated probability.
                
                {
                  "probability": 0.04,
                  "label": "<=50K",
                  "status": "OK",
                  "request_id": 1
                }
                
 Now you have a working ML Web Service.
 
 
### Notes:
  1. This Repo was just made for educational purpose
  2. The Following tutorial shows you how to create similar repo like this in Details --> Credits @Piotr Płoński
      https://www.deploymachinelearning.com/
