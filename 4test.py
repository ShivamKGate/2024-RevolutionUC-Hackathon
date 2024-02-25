from taipy import Gui
import pandas as pd

# Load the data
data = pd.read_csv('C:\\Users\\skhar\\Downloads\\2024-RevolutionUC-Hackathon\\HealthSphere\\data2.csv')

# Count the occurrences of each unique condition
status_counts_updated = data['Condition'].value_counts()
print(status_counts_updated)
myList = []

for keys in status_counts_updated.keys():
    myList.append((keys, status_counts_updated[keys]))  # Using strip() to remove leading/trailing spaces
my_data = pd.DataFrame(myList, columns=['Condition', 'Count'])
print(my_data)
# Define the GUI page to include a pie chart based on 'Condition' and 'Phase'
page = """
# Phase vs Condition
<|{my_data}|chart|type=pie|values=Count|labels=Condition|>
"""

# Initialize and run the GUI instance
gui_instance = Gui(page)
gui_instance.run(use_reloader=False)  # Set 'use_reloader' to False for simplicity in this example
