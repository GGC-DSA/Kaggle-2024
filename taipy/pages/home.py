from taipy.gui import Markdown, Gui, State, navigate
import pandas as pd


df = pd.read_json("taipy/train.json")
app_page = f"application_md"

def go_to_app(state):
  navigate(state=state, to="App")
        


home_md = Markdown("""
----------------                   
<h1>Project: Identifying PII in Student Essays</h1>
                  
<h3>[Placeholder for model screenshot image/demo]</h3>
                  
<|Get Started|button|hover_text="Click to go test your text!"|on_action=go_to_app|>
                  



           
                   

                   

----------------

# About                        
### The goal of this competition is to develop a model that detects sensitive personally identifiable information (PII) in student writing. This is necessary to screen and clean educational data so that when released to the public for analysis and archival, the risk to the students is mitigated.
                  
# Dataset
### [Click here](http://www.kaggle.com/c/pii-detection-removal-from-educational-data) to navigate to the Kaggle site containing the official datasets: 

----------------  
                         
## Training Data
          
<|{df}|table|>
                  
""")