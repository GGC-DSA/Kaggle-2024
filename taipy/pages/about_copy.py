import pandas as pd
import taipy.gui.builder as tgb
from taipy.gui import Gui, Page, State


class About(Page):
    # def __init__(self):
    #     self.food_df = pd.DataFrame({
    #         "Meal": ["Lunch", "Dinner", "Lunch", "Lunch"],
    #         "Category": ["Food", "Food", "Drink", "Food"],
    #         "Name": ["Burger", "Pizza", "Soda", "Salad"],
    #         "Calories": [300, 400, 150, 200],
    #     })
    #     super().__init__()

    def create_page(self):
        with tgb.Page() as page:
            tgb.text("""
              ----------------                                       
              <h1>About The Project</h1>
              <h3>The goal of this competition and project is to develop a model that detects sensitive personally identifiable information (PII) in student writing. This is necessary to screen and clean educational data so that when released to the public for analysis and archival, the risk to students having their data used improperly is mitigated. </h3>
                                
              ----------------
                                
              <center><h1>Meet Our Team: The Algorithm Allies!</h1></center>
              ----------------

              <center><h2>&emsp; &emsp; Manu Achar &emsp; &emsp; &emsp; &emsp; &emsp; &emsp;Cody Ledford &emsp; &emsp; &emsp; &emsp;Pratik Chaudhari</h2></center>

              <center>[![Manu Achar](images/ManuA.jpg)](images/ManuA.jpg) &emsp; [![Cody Ledford](images/CodyL.jpg)](images/CodyL.jpg) &emsp; [![Pratik Chaudhari](images/PratikC.png)](images/PratikC.png)</center>

              """, mode="md")
        return page

if __name__ == '__main__':
    Gui(page=About()).run()