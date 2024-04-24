from taipy import Config
import taipy as tp
from taipy.gui import Markdown, Gui
import taipy.gui.builder as tgb
import pandas as pd
import numpy as np

train_file = pd.read_json("datasets/Official/train.json")
sub_file = pd.read_csv("datasets/Official/sample_submission.csv")

sample_file = pd.DataFrame(train_file.head(n=1))
sample_output = pd.DataFrame(sub_file.head())

# print(sample_file)
# print(sample_output)

with tgb.Page() as application:
  tgb.text("# Upload a copy of your text file* you would like to identify PII in.", mode="md")
  tgb.file_selector(label="Select File", extensions=".txt")
  tgb.table(data=train_file.head())

application_md= ("""
----------------
# Upload a copy of your text file* you would like to identify PII in.
                               
<|{content}|file_selector|label=Select File|extensions=.txt|>
                

<|{train_file}|table|>             
                 
                            
### *File must be in .txt format
                    
----------------
                 
## Your Report:

<|{sample_output}|table|>                 

### Download your PII Report:
                                        
<|{"../taipy/message.txt"}|file_download|>
------
""")

# ### Message: <|{message}|text|>
# # Name: <|{input_name}|input|> <|submit|button|on_action=submit_scenario|>