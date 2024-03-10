"""
The following website was used to create this Hello World
application that will be hosted on the taipy cloud community
edition for free.

https://docs.taipy.io/en/latest/getting_started/
"""

from taipy import Config
import taipy as tp
import os
from tempfile import NamedTemporaryFile

# Stores the path to the temporary file - this is broken
temp_path = "taipy/message.txt"

def build_message(name: str):
    return f"Hello {name}! I am so glad that you are here!"

def save_message(message: str):
    directory = "../taipy/"  # Adjust the directory as needed
    filepath = os.path.join(directory, "message.txt")
    with open(filepath, "w") as file:
        file.write(message)


# Remove the temporary file
def clean_up(state):
    os.remove(state.temp_path + "message.txt")

# def download(state, content, name, on_action):
#     print(f"Downloading {name}...")
#     # Here you would implement the logic to handle the file download.
#     with open(state.temp_path + "message.txt", wb) as file:
#         file.write(wb)
#     print(f"Download complete: {name}")
#     # Call the provided on_action function if it's callable
#     if callable(on_action):
#         on_action(state)
    
def download(state, filename, on_action):
    try:
        file_url = f"../taipy/{filename}"  # Adjust the path as needed
        return f"<a href='{file_url}' download>Download {filename}</a>"
    except Exception as e:
        print(f"An error occurred while generating download link: {e}")

    
# def download(state, filename, on_action):
#     try:
#         return send_from_directory("taipy", filename, as_attachment=True)
#     except Exception as e:
#         print(f"An error occurred while downloading the file: {e}")

# In your route or view function where you handle the download action:
# @app.route('/download/<filename>')
# def download_file(filename):
#     return download(state, filename, on_action=clean_up)

# Generate the message, save them in a CSV temporary file, then trigger a download action
# for that file.
# def download_pi(state):
#     message = state.message
#     with NamedTemporaryFile("w", suffix=".txt", delete=False) as temp_file:
#         temp_file.write(message)
#         state.temp_path = temp_file.name

#     try:
#         hello_scenario = tp.create_scenario(scenario_cfg)
#         hello_scenario.input_name.write("Pratik")
#         hello_scenario.submit()
#         message = hello_scenario.message.read()
#         if message:
#             save_message(message)
#             print("Message saved to 'message.txt'.")
#         else:
#             print("Error: No message received from the scenario.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     download(state, content=state.temp_path, name="message.txt", on_action=clean_up)
        
def download_pi(state):
    message = state.scenario.message.read()
    try:
        save_message(message)
        print("Message saved to 'message.txt'.")
        download(state, "message.txt", on_action=save_message)
    except Exception as e:
        print(f"An error occurred while saving the message: {e}")


input_name_data_node_cfg = Config.configure_data_node(id="input_name")
message_data_node_cfg = Config.configure_data_node(id="message")
#dowload_file_task_cfg = Config.configure_task("download_pi", download_pi, message_data_node_cfg)
save_message_task_cfg = Config.configure_task("save_msg", save_message, message_data_node_cfg)
build_msg_task_cfg = Config.configure_task("build_msg", build_message, input_name_data_node_cfg, message_data_node_cfg)
scenario_cfg = Config.configure_scenario("scenario", task_configs=[build_msg_task_cfg, save_message_task_cfg])
#scenario_cfg = Config.configure_scenario("scenario", task_configs=[build_msg_task_cfg, dowload_file_task_cfg])


# Previous configuration of scenario
...
content = "message.txt"

page = """
Name: <|{input_name}|input|>
<|submit|button|on_action=submit_scenario|>


Message: <|{message}|text|>


### Download your message:

<|{None}|file_download|on_action=download_pi|>
------

# Meet Our Team:
----------------

## &emsp; &emsp; Manu Achar &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; Cody Ledford &emsp; &emsp; &emsp; &emsp; Pratik Chaudhari

[![Manu Achar](images/ManuA.jpg)](images/ManuA.jpg) &emsp; [![Cody Ledford](images/CodyL.jpg)](images/CodyL.jpg) &emsp; [![Pratik Chaudhari](images/PratikC.png)](images/PratikC.png)




"""
# The exclamation mark in the markdown above is used to signify that the link passed in should be 
# an image, and should display the image inline rather than a link, which is what would happen if
# we were to use the same thing without an exclamation mark.

# &emsp; is an HTML entity that will create a consistent empty space - it creates a space equal to the current font size which also ensures consistency.

# <|{content}|file_download|>

# The commented out code was to try and get a custom button. Need to
# look up the on_action allowed variables and what they are able to do.
# <|Download File|button|{content}|file_download|on_action=file_download|auto|>

input_name = "Enter Name Here"
message = None


def submit_scenario(state):
    state.scenario.input_name.write(state.input_name)
    state.scenario.submit(wait=True)
    state.message = scenario.message.read()


if __name__ == "__main__":
    tp.Core().run()
    scenario = tp.create_scenario(scenario_cfg)
    tp.Gui(page).run(use_reloader=True)

