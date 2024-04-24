from taipy import Config
import taipy as tp
from taipy.gui import Markdown, Gui

about_md = Markdown("""
----------------                                       
<h1>About The Project</h1>
<h3>The goal of this competition and project is to develop a model that detects sensitive personally identifiable information (PII) in student writing. This is necessary to screen and clean educational data so that when released to the public for analysis and archival, the risk to students having their data used improperly is mitigated. </h3>
                   
----------------
<h1>Technologies</h1>
BERT - Fine-Tuned
PyTorch
Taipy & Taipy Cloud
Docker & DockerHub
Plotly
Pandas
Numpy

                       
----------------                  
                   
<center><h1>Meet Our Team: The Algorithm Allies!</h1></center>
----------------

<center><h2>&emsp; &emsp; Manu Achar &emsp; &emsp; &emsp; &emsp; &emsp; &emsp;Cody Ledford &emsp; &emsp; &emsp; &emsp;Pratik Chaudhari</h2></center>

<center>[![Manu Achar](images/ManuA.jpg)](images/ManuA.jpg) &emsp; [![Cody Ledford](images/CodyL.jpg)](images/CodyL.jpg) &emsp; [![Pratik Chaudhari](images/PratikC.png)](images/PratikC.png)</center>

""")