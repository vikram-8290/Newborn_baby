# Newborn_baby

# About The Project
This project involves building a web application using Flask to predict post-transfusion hemoglobin levels for newborn babies. The application takes input data such as the baby's age (in days), initial hemoglobin level, and the volume of the transfusion given. It then uses a machine learning model (loaded from a pickle file) to predict the post-transfusion hemoglobin level.

The project includes the following components:

Flask Web Application:  A Flask web application with routes for the homepage, prediction API endpoint (/predict_api), and a route to handle form submissions (/predict). The application uses HTML templates to display forms, messages, and results.

Machine Learning Model: A regression model (linear regression) using some dataset to predict the post-transfusion hemoglobin levels. The trained model is saved as a pickle file (regmodel.pkl) and loaded into the Flask app.

Input Form: The web application displays an input form on the homepage where users can enter the baby's age, initial hemoglobin level, and transfusion volume. Upon submission, the form data is sent to the /predict route for processing.

Result Display: After submitting the form, the application uses the trained model to predict the post-transfusion hemoglobin level. The result is displayed to the user as a predicted hemoglobin value and, in some cases, a percentage change compared to the initial hemoglobin level.

Handling Edge Cases: The code has been modified to handle cases where the initial hemoglobin level is close to zero to avoid division by zero errors and provide meaningful results.


Overall, project aims to provide a user-friendly interface to predict post-transfusion hemoglobin levels for newborn babies based on input data and a trained regression model. 




# Applications Used

1. Pyhton 3
2. Jupyter Notebook
3. Github Account
4. IDLE
5. GitCLI

# create an Environment 
```
    conda create -p venv python=3.7.8 -y
```


# Run Locally

Navigate to The Folder 

Run
```
python3 app.py
```