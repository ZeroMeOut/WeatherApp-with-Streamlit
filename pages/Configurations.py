import streamlit as st

import json
import subprocess
from utilities import locator
from time import sleep


# For Binary Search, this part doesn't work really well for some reason
def binary_search(list_of_dicts, key, target):
    low = 0
    high = len(list_of_dicts) - 1

    while low <= high:
        mid = (low + high) // 2
        current_dict = list_of_dicts[mid]

        if target == current_dict.get(key):
            return current_dict
        elif target < current_dict.get(key):
            high = mid - 1
        else:
            low = mid + 1

    return None

if 'pid' not in st.session_state:
    st.session_state.pid = None

python_executable = 'weatherevenv/Scripts/python.exe' # You may need to change this for your environment
python_script = 'producer.py'
command = [python_executable, python_script]

st.title('Configure')

api_key = st.text_input('API Key', value = "") # Gets the api key from the user
user_input = st.text_input('Input location') # Gets the user input

locator = locator.Locator(user_input)
locations = locator.lonlat()

display_names = [location['display_name'] for location in locations]

target = st.selectbox(
    'Select a location',
    display_names
)

selected_location = binary_search(locations, 'display_name', target) # Gets the selected location

if selected_location is not None:
    if st.session_state.pid is not None:
         subprocess.run(['taskkill', '/F', '/PID', str(st.session_state.pid)])

    data = {'lat': selected_location['lat'], 'lon': selected_location['lon'], 'api_key': api_key}

    jsonString = json.dumps(data)
    jsonFile = open("data.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()

    process = subprocess.Popen(command)

    st.session_state.pid = process.pid

else:
    if st.session_state.pid is not None:
        subprocess.run(['taskkill', '/F', '/PID', str(st.session_state.pid)])
    
    st.session_state.pid = None





    



    