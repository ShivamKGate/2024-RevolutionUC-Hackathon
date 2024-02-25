import taipy
import pandas as pd
nb_points = 10000
data1 = pd.read_csv('data.csv')
page = """
#Enrollment vs Year
<|{nb_points}|slider|min=10000|max=15000|>
<|{data1[:nb_points]}|chart|min=1980|max=2025|>
"""
# # Read the data
data2 = pd.read_csv('data1.csv')

# Count the occurrences of each unique status
status_counts_updated = data2['Status'].value_counts()

myList = []

for keys in status_counts_updated.keys():
    myList.append((keys, status_counts_updated[keys]))

my_data = pd.DataFrame(myList, columns=['Status', 'Count'])

page += """
#Status vs Count
<|{my_data}|chart|type=bar|x=Status|y=Count|>
"""

data3 = pd.read_csv('data2.csv')

# Count the occurrences of each unique condition
status_counts_updated = data3['Condition'].value_counts()
myList = []

for keys in status_counts_updated.keys():
    myList.append((keys, status_counts_updated[keys]))  # Using strip() to remove leading/trailing spaces
my_data2 = pd.DataFrame(myList, columns=['Condition', 'Count'])
# Define the GUI page to include a pie chart based on 'Condition' and 'Phase'
page += """
# Phase vs Condition
<|{my_data2}|chart|type=pie|values=Count|labels=Condition|>
"""

    # Load the data
data4 = pd.read_csv('data2.csv')

# Count the occurrences of each unique condition
status_counts_updated = data4['Condition'].value_counts()

my_data3 = {
    "Condition": status_counts_updated.index.tolist(),
    "Count": status_counts_updated.values.tolist()
}

options = {
    # Fill to x axis
    "fill": "tozeroy"
}
# Define the GUI page to include a pie chart based on 'Condition' and 'Phase'
page += """
# Phase vs Condition
<|{my_data3}|chart|x=Count|y=Condition|options={options}|>
"""

gui_instance = taipy.Gui(page)
print(gui_instance)
gui_instance.run(ngrok_token="2crQnYdkbwmjqMTdjlNna5yt2Al_7fN6yvYnkbgqKNWPJJsGd")