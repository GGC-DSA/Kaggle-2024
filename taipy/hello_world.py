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


def build_message(name: str):
    return f"Hello {name}! I am so glad that you are here!"

def save_message(message: str):
    with open("message.txt", "w") as file:
        file.write(message)


# Stores the path to the temporary file - this is broken
temp_path = "../taipy/"

# Remove the temporary file
def clean_up(state):
    os.remove(state.temp_path + "message.txt")

def download(state, content, name, on_action):
    print(f"Downloading {name}...")
    # Here you would implement the logic to handle the file download.
    print(f"Download complete: {name}")
    # Call the provided on_action function if it's callable
    if callable(on_action):
        on_action(state)

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
        download(state, state.message,"message.txt", on_action=None)
    except Exception as e:
        print(f"An error occurred while saving the message: {e}")


input_name_data_node_cfg = Config.configure_data_node(id="input_name")
message_data_node_cfg = Config.configure_data_node(id="message")
dowload_file_task_cfg = Config.configure_task("download_pi", download_pi, message_data_node_cfg)
build_msg_task_cfg = Config.configure_task("build_msg", build_message, input_name_data_node_cfg, message_data_node_cfg)
scenario_cfg = Config.configure_scenario("scenario", task_configs=[build_msg_task_cfg, dowload_file_task_cfg])


# Previous configuration of scenario
...
content = "message.txt"

page = """
Name: <|{input_name}|input|>
<|submit|button|on_action=submit_scenario|>

Message: <|{message}|text|>

### Download your message:
<|{None}|file_download|on_action=download_pi|>

"""
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
    tp.Gui(page).run()

