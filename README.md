# Kaggle-2024

# Spring 2024 Team
Manu Achar - Project Manager and Data Modeler

Cody Ledford - Data Analyzer and Client Liaison

Pratik Chaudhari - Document Manager and Data Visualizer

# Description
Our team is the Algorithm Allies! We are working on a Kaggle project via their Challenges section. Our client will be Dr. Gunay.

The Kaggle Competition we are participating in is the [PII Data Detection hosted by The Learning Agency Lab](https://www.kaggle.com/competitions/pii-detection-removal-from-educational-data/overview). The objective of the project is to create an AI model that detects personal identifiable information (PII) so they can be censored. This is important when releasing educational material to the public to protect the identity of students. The data is contained in JSONs of student essays that were tokenized using [spaCy](https://spacy.io/).

---

# Links
* [Project Website](https://ggc-dsa.github.io/Kaggle-2024/)
* [Inference Notebook](code/AlgAllies-PII-Inference.ipynb)
* [Training Notebook](code/AlgAllies-PII-Training.ipynb)
* [Vlogs](media)
* [Final Report](docs-Spr2024/Report.pdf)

# Presentations
* STaRS @ GGC on 4/11/2024 - won honorable mention / [Poster](docs-Spr2024/Alg_Allies_Kaggle_Poster_STARS.pdf)
* CREATE Symposium @ GGC on 4/25/2024 - presented / [Project Website](https://ggc-dsa.github.io/Kaggle-2024/)

# Technologies
* Jupyter Notebooks
    * Kaggle
    * Google Colab
* PyTorch
* BERT
* Taipy
* JavaScript
* HTML/CSS
* Bootstrap
* Git LFS
* GitHub
* Docker
* DockerHub

---

# Git LFS

Since the size of the dataset is larger than 100 MB - the limit for GitHub, you must install Git LFS:

* The first stepm is to install Git LFS

`install git lfs`

* Start file tracking for git lfs in the repo

`git lfs track *.json`

After cloning the repo locally, it clones the Git LFS pointer file, not the data file. To get the data file itself run this:

`git lfs pull`




# Taipy Section

This project uses [Taipy](https://www.taipy.io/). You will needed to run the following code in your command prompt (be sure to run as administrator) 
```
pip install taipy
```

This will enable you to properly run the taipy application locally. The project will be accessible and able to run in the cloud environment provided by Taipy. 

To run the application locally, you will need to navigate to the directory where you have the repo cloned, into the taipy folder e.g.(C:\Users\user1\Desktop\Kaggle-2024\taipy\main.py), and in your command prompt, terminal, or bash terminal, use "python3 main.py" to run the file and see the application using your local machine.

This will bring up a browser window which is hosted on port 5000 on your local machine. The ip address should show as your loopback number (127.0.0.1:8888). Upon success, this is where you continue to use the application. 

## How to use the application

### The goal of this application is to leverage our machine learning model to accept user input of a few words, sentences, or paragraphs in efforts to properly identify PII. The required input is a text file.

We will be populating a document of all the identified PII to a file, for which you can download at your convienience.

If so desired, you can run the program as many times as you would like and pull as many reports after running as you would like.

The following are the tags that should be identified in your text containing PII: ["B-EMAIL", "B-ID_NUM", "B-NAME_STUDENT", "B-PHONE_NUM",
              "B-STREET_ADDRESS", "B-URL_PERSONAL", "B-USERNAME",
              "I-ID_NUM", "I-NAME_STUDENT", "I-PHONE_NUM",
              "I-STREET_ADDRESS","I-URL_PERSONAL"]

Using these predefined labels to train our model, our model should be able to properly tokenize, label, and report on the data that you provide. B-records indicate the beginning of PII data. I-records indicate the continuation of PII data.

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
```

Optionally, you can navigate to the directory where the requirements.txt file is located, and run ```pip install -r requirements.txt``` - this will properly install all of the libraries and modules that are required by the application to run.

## Our Usage

There are 4 main parts of the web application page:
- The Home Page
- The About Page
- The App Page
- The Graphs Page

### The Home Page
The goal of the home page was to provide a nice landing area, where there is a button that will take you straight to the application page, and there is also a summarization of the data that was used for training.

### The About Page
The goal of the about page was simply to provide information about the project, and show the team as it were. There wasn't much other intent behind this page other than that.

### The App Page
This is the main reason for using Taipy. We wanted to make a web application that enables our model to be used by anyone and everyone. The app page is complete with the buttons that allow users to upload their text files, and download their reports.

**At the time of creation of this README, there are non-functional pieces to this page in the site. The following has not yet been implemented**
 - The model has not yet been added to the application, so it is not possible in current state to have your text processed via the web application.
 - The upload functionality is mostly working, however, since there was an inability to test with a server of sorts outside of our local machines, we were unable to enable functionality that would gurantee saving a file - even for intermediate use.
 - There is no tokenization process built into the web application. This sort of feeds off of the previous point, but without the ability to have a file uploaded by the user, we were unable to work with the text in any manner for processing.
 - The download report functionality is incomplete. In it's current state, the download function will only provide the results in the browser window, rather than downloading a file to your computer. I think this is also compounded off the need for a server, since it would be different behavior for the application to have the file downloadable to a user's machine rather than copying a local file to a new directory.
 - The table previews are not currently working. The intention was, whenever a user uploads a text file to be processed, they would see a preview of it, similar to how you see a preview in the home page. It was also the intent to show a preview of the report that gets generated. This was not able to be properly implemented, as there was some sort of scoping issue with the application that was attempted to be resolved with Taipy devs via their discord.

 Other than the things highlighted here, the application page is able to be navigated to and worked with, albeit lacking functionality.

 ### The Graph Page
 The graph page of the site uses Plotly in the backend, which allows for us to directly interact with the visualizations inside of the web app. 

 Currently, 2 out of 3 visualizations added are leveraging plotly, with the 3rd still needing to be updated from a png/jpg file into a direct plotly graph.

 # End Taipy Section



 # Project Results
 * Static website
    * Analysis/Visualizations
    * Link to taipy app
 * Model trained on the student essays dataset to detect PII and provide a report providing location and type of PII.
 * Taipy web app
    * File upload
    * Interactive Visualizations
    * Dataset Preview

## Datasets
* [Official](https://github.com/GGC-DSA/Kaggle-2024/tree/main/datasets/Official) - provided by the Kaggle competition
* [External](https://github.com/GGC-DSA/Kaggle-2024/tree/main/datasets/External) - aggregated from pertinent Kaggle datasets outside the competition

## Main methods for analysis and plots
As we were working out our model inputs, we wanted to see the length of essays. Since out models input was limited to 512, we had to see if the essays would fit in that range.

![Essay Lengths](media/essay_lengths.png)

We used a t-test to evalute the claim that at least one PII was in each essay. We found that the claim of at least one PII per essay was support by the data.

![PII Distribution](docs/assets/img/graphs/pii_distribution.png)

Next we ran two Tukey tests, the first to determine whether NAME_STUDENT_PII has a greater likelihood to appear than other PII. We found this to be true, shown as well in the plot below.

![Most Common Types PII](docs/assets/img/graphs/most_common_pii.png)

The next Tukey test was to determine what part of the essay the PII is located in. Each essay was split into five parts and the PII was marked under the section it appeared in. We found that the PII data was found in the first part of five more than the other parts.

![Location of PII](docs/assets/img/graphs/pii_location.png)


# TODO - Remaining Scope
* Use different preprocessing methods 
* Try more rebalancing or different hyperparameters 
* Try to use a different pre-trained model like RoBERTA or distilBERT 
* Supplement training with the additional datasets found 
* Add model to Taipy site 
* Find a host for the Taipy site