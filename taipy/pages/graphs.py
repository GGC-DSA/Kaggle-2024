                #################################
                ###       Graph Section       ###
                #################################
from taipy.gui import Markdown, State
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

# Load in the dataset
df = pd.read_json("taipy/train.json")
# print(df.head()) 

"""
These markdown elements were previously used to place the image of the various graphs onto the webpage, but now we are able to take the approach of directly embedding the graphs into the webpage.

[![PII Type Frequency Graph](images/Frequency_PII_Types.jpg)](images/Frequency_PII_Types.jpg)
"""

              #################################
              ###       PII Frequency       ###
              #################################

# Process the dataframe and count the occurrences of elements within the labels column
c = Counter()
df.apply(lambda line: c.update(line.labels), axis = 1)
c_pii = c.most_common()[1:]
c_key, c_val = zip(*c_pii)

# Add the values for the frequency of PII labels to a dictionary for calling in the visualization
pii_freq = pd.DataFrame({'Label': c_key, 'Count': c_val})

              #################################
              ###       PII Proportion      ###
              #################################

"""
# This section is leveraging matplotlib, which executes in a new window. You can uncomment to check it out.

labels = df['labels']

non_o_values = df.apply(lambda line: sum(1 for x in line['labels'] if x != 'O')/ len(line['labels']), axis = 1)

print(non_o_values)

proportions_array = np.array(non_o_values)

print(proportions_array)

plt.hist(proportions_array, bins=20, color='blue', edgecolor='black', alpha=0.7)
plt.xlabel('Proportion of PII Values in Text')
plt.ylabel('Frequency (Log Scaled)')
plt.title('Distribution of PII Values in Text')
plt.yscale('log')
plt.show()
"""
labels = df['labels']

non_o_values = df.apply(lambda line: sum(1 for x in line['labels'] if x != 'O')/ len(line['labels']), axis = 1)

proportions_array = np.array(non_o_values)

hist, bin_edges = np.histogram(proportions_array, bins=20)

# hist = np.log(hist + 1)

bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

bin_centers = bin_centers * 100

hist_df = pd.DataFrame({
    'Percentage': bin_centers,
    'Count': hist
})

              #################################
              ###        PII Position       ###
              #################################

graphs_md = Markdown("""
----------------                         
<h1>Proportion of PII in Essay Data</h1>
                    
<|{hist_df}|chart|type=bar|x=Percentage|y=Count|title=Percentage of PII Values in Text|>
                    
<h1>Frequency of PII Types in Essay Data</h1>
                    
<|{pii_freq}|chart|type=bar|x=Label|y=Count|title=Frequency of PII Types|>
                    
<h1>Position of PII Types in Essay Data</h1>
                    
[![PII Position Graph](images/PII_Positions.png)](images/PII_Positions.png)
----------------
""")