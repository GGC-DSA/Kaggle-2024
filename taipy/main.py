<<<<<<< HEAD
"""
The following website was used to create this Hello World
application that will be hosted on the taipy cloud community
edition for free.

https://docs.taipy.io/en/latest/getting_started/
"""

from taipy import Config
import taipy as tp
import os
from pages.about import about_md
from pages.application import application_md
from pages.application import application
from pages.graphs import graphs_md
from pages.home import home_md
from pages.root_page import root_page
import taipy.gui.builder as tgb
from pages.about_copy import About

# Stores the path to the temporary file - this is broken
temp_path = "../taipy/message.txt"

about_page = About()

##################################################################

def build_message(name: str):
    message = f"Hello {name}! I am so glad that you are here!"
    save_message(message)
    return message

def save_message(message: str):
    directory = "../taipy/"  # Adjust the directory as needed
    filepath = directory + "message.txt"
    with open(filepath, "w") as file:
        file.write(message)
        file.close()


# Remove the temporary file
def clean_up(state):
    os.remove(state.temp_path + "message.txt")
        
# Logic for downloading the file
def download_pi(state):
    message = state.scenario.message.read()
    try:
        save_message(message)
        print("Message saved to 'message.txt'.")
        # download(state, "message.txt", on_action=save_message)
    except Exception as e:
        print(f"An error occurred while saving the message: {e}")

# def submit_scenario(state):
#     state.scenario.input_name.write(state.input_name)
#     state.scenario.submit(wait=True)
#     state.message = scenario.message.read()
#     save_message(scenario.message.read())

##################################################################

# input_name_data_node_cfg = Config.configure_data_node(id="input_name")
# message_data_node_cfg = Config.configure_data_node(id="message")
# dowload_file_task_cfg = Config.configure_task("download_pi", download_pi, message_data_node_cfg)
# save_message_task_cfg = Config.configure_task("save_msg", save_message, message_data_node_cfg)
# build_msg_task_cfg = Config.configure_task("build_msg", build_message, input_name_data_node_cfg, message_data_node_cfg)
# scenario_cfg = Config.configure_scenario("scenario", task_configs=[build_msg_task_cfg])
# scenario_cfg = Config.configure_scenario("scenario", task_configs=[build_msg_task_cfg, dowload_file_task_cfg])

##################################################################

# Previous configuration of scenario
...
content = "message.txt"

""" 
The exclamation mark in the markdown above is used to signify that the link passed in should be an image, and should display the image inline rather than a link, which is what would happen if we were to use the same thing without an exclamation mark.


&emsp; is an HTML entity that will create a consistent empty space - it creates a space equal to the current font size which also ensures consistency.
"""

input_name = "Enter Name Here"
message = None

pages = {   
            "/": root_page,
            "Home": home_md,
            "About": about_md,
            "App": application_md,
            "Graphs": graphs_md
         }

if __name__ == "__main__":
    tp.Core().run()
    # scenario = tp.create_scenario(scenario_cfg)
    tp.Gui(pages=pages).run(use_reloader=True, port=8888, title="PII Detective")

=======
"""
The following website was used to create this Hello World
application that will be hosted on the taipy cloud community
edition for free.

https://docs.taipy.io/en/latest/getting_started/
"""

from taipy import Config
import taipy as tp
import os
from pages.about import about_md
from pages.application import application_md
from pages.application import application
from pages.graphs import graphs_md
from pages.home import home_md
from pages.root_page import root_page
import taipy.gui.builder as tgb
from pages.about_copy import About

# Stores the path to the temporary file - this is broken
temp_path = "../taipy/message.txt"

about_page = About()

##################################################################

def build_message(name: str):
    message = f"Hello {name}! I am so glad that you are here!"
    save_message(message)
    return message

def save_message(message: str):
    directory = "../taipy/"  # Adjust the directory as needed
    filepath = directory + "message.txt"
    with open(filepath, "w") as file:
        file.write(message)
        file.close()


# Remove the temporary file
def clean_up(state):
    os.remove(state.temp_path + "message.txt")
        
# Logic for downloading the file
def download_pi(state):
    message = state.scenario.message.read()
    try:
        save_message(message)
        print("Message saved to 'message.txt'.")
        # download(state, "message.txt", on_action=save_message)
    except Exception as e:
        print(f"An error occurred while saving the message: {e}")

# def submit_scenario(state):
#     state.scenario.input_name.write(state.input_name)
#     state.scenario.submit(wait=True)
#     state.message = scenario.message.read()
#     save_message(scenario.message.read())

##################################################################

# input_name_data_node_cfg = Config.configure_data_node(id="input_name")
# message_data_node_cfg = Config.configure_data_node(id="message")
# dowload_file_task_cfg = Config.configure_task("download_pi", download_pi, message_data_node_cfg)
# save_message_task_cfg = Config.configure_task("save_msg", save_message, message_data_node_cfg)
# build_msg_task_cfg = Config.configure_task("build_msg", build_message, input_name_data_node_cfg, message_data_node_cfg)
# scenario_cfg = Config.configure_scenario("scenario", task_configs=[build_msg_task_cfg])
# scenario_cfg = Config.configure_scenario("scenario", task_configs=[build_msg_task_cfg, dowload_file_task_cfg])

##################################################################

# Previous configuration of scenario
...
content = "message.txt"

""" 
The exclamation mark in the markdown above is used to signify that the link passed in should be an image, and should display the image inline rather than a link, which is what would happen if we were to use the same thing without an exclamation mark.


&emsp; is an HTML entity that will create a consistent empty space - it creates a space equal to the current font size which also ensures consistency.
"""

input_name = "Enter Name Here"
message = None

pages = {   
            "/": root_page,
            "Home": home_md,
            "About": about_md,
            "App": application_md,
            "Graphs": graphs_md
         }

if __name__ == "__main__":
    tp.Core().run()
    # scenario = tp.create_scenario(scenario_cfg)
    tp.Gui(pages=pages).run(use_reloader=True, port=8888, title="PII Detective")

>>>>>>> 96b9c6dbdbcd3e4c3cb1f609f4a93248b0c9b985
