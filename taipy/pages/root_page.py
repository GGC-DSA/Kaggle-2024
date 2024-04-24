from taipy import Config
import taipy as tp
from taipy.gui import Markdown, Gui, State
import taipy.gui.builder as tgb
import webbrowser

ggc_logo = "../Kaggle-2024/taipy/images/GGC_Logo.png"

ggc_website = "https://www.ggc.edu/academics/school-of-science-and-technology/information-technology"

##################CSS Section################################

# logo = { 
    
# }

##################Function Section###########################

def go_to_site():
        webbrowser.open(f'{ggc_website}')  # Go to example.com

with tgb.Page() as root_page:
    tgb.image("{ggc_logo}", label="Click to see GGC Website", on_action=go_to_site, class_name="inline", width="10vw", height="18vh")
    tgb.navbar()
    tgb.toggle(theme=True, active=True)
from taipy import Config
import taipy as tp
from taipy.gui import Markdown, Gui, State
import taipy.gui.builder as tgb
import webbrowser

ggc_logo = "../Kaggle-2024/taipy/images/GGC_Logo.png"

ggc_website = "https://www.ggc.edu/academics/school-of-science-and-technology/information-technology"

##################CSS Section################################

# logo = { 
    
# }

##################Function Section###########################

def go_to_site():
        webbrowser.open(f'{ggc_website}')  # Go to example.com

with tgb.Page() as root_page:
    tgb.image("{ggc_logo}", label="Click to see GGC Website", on_action=go_to_site, class_name="inline", width="10vw", height="18vh")
    tgb.navbar()
    tgb.toggle(theme=True, active=True)