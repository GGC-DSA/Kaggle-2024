# Kaggle-2024
---
# Spring 2024 Team
---
Manu Achar - Project Manager and Data Modeler

Cody Ledford - Data Analyzer and Client Liaison

Pratik Chaudhari - Document Manager and Data Visualizer

# Description
---
Our team is the Algorithm Allies! We are working on a Kaggle project via their Challenges section. Our client will be Dr. Gunay.

The Kaggle Competition we are participating in is the [PII Data Detection hosted by The Learning Agency Lab](https://www.kaggle.com/competitions/pii-detection-removal-from-educational-data/overview). The objective of the project is to create an AI model that detects personal identifiable information (PII) so they can be censored. This is important when releasing educational material to the public to protect the identity of students. The data is contained in JSONs of student essays that were tokenized using [spaCy](https://spacy.io/).

This project uses [Taipy](https://www.taipy.io/). You will needed to run the following code in your command prompt (be sure to run as administrator) 
```
pip install taipy
```

This will enable you to properly run the taipy application locally. The project will be accessible and able to run in the cloud environment provided by Taipy. 

To run the application locally, you will need to navigate to the directory where you have the repo cloned, into the taipy folder e.g.(C:\Users\user1\Desktop\Kaggle-2024\taipy\hello_world.py), and in your command prompt, terminal, or bash terminal, use "python3 hello_world.py" to run the file and see the application using your local machine.

This will bring up a browser window which is hosted on port 5000 on your local machine. The ip address should show as your loopback number (127.0.0.1:5000). Upon success, this is where you continue to use the application. 

*A brief outline of the application which should be updated later.*

# How to use the application
### The goal of this application is to leverage our machine learning model to accept user input of a few words, sentences, or paragraphs in efforts to properly identify PII
We will be populating all the identified PII to a file, for which you can download at your convienience.
If so desired, you can run the program as many times as you would like and pull as many reports after running as you would like.

There will be an indicator which will reflect the level of confidence of our model in identifying your PII in the provided information. 

The following are the tags that should be identified in your text containing PII: ["B-EMAIL", "B-ID_NUM", "B-NAME_STUDENT", "B-PHONE_NUM",
              "B-STREET_ADDRESS", "B-URL_PERSONAL", "B-USERNAME",
              "I-ID_NUM", "I-NAME_STUDENT", "I-PHONE_NUM",
              "I-STREET_ADDRESS","I-URL_PERSONAL","O"]

Using these predefined labels to train our model, our model should be able to properly tokenize, label, and report on the data that you provide. B-records indicate the beginning of PII data. I-records indicate the continuation of PII data. O-records indicate that the token (text) is not identified as containing the pre-defined labels of PII.

*Step-by-step instructions to follow*

In order to run the notebook containing the model which leverages NER and NLP to properly identify PII, there are some preliminary steps that you need to take to ensure that you have all of the necessary libraries and modules installed on your local machine.


We will be using the following libraries and modules:
torch
keras
keras_nlp
ops
tensorflow
json
numpy
pandas
tqdm.notebook
sklearn
plotly

- To ensure that you have all of the dependencies downloaded, run the following commands as an administrator in your command prompt:

```
pip install torch
pip install keras
pip install keras_nlp
pip install tensorflow
pip install numpy
pip install pandas
pip install tqdm
pip install sklearn
pip install plotly

Optionally, you can navigate to the directory where the requirements.txt file is located, and run pip install requirements.txt - this will properly install all of the libraries and modules that are required by the application to run.
```