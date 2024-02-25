from taipy import gui
import pandas as pd

# Read the data
data = pd.read_csv('C:\\Users\\skhar\\Downloads\\2024-RevolutionUC-Hackathon\\HealthSphere\\data1.csv')
print(data)

# Count the occurrences of each unique status
status_counts_updated = data['Status'].value_counts()

myList = []

for keys in status_counts_updated.keys():
    myList.append((keys, status_counts_updated[keys]))

my_data = pd.DataFrame(myList, columns=['Status', 'Count'])
print(my_data)

page = """
#Status vs Count
<|{my_data}|chart|type=bar|x=Status|y=Count|>
"""

# Correcting the usage of the `gui` module
gui_instance = gui.Gui(page)
gui_instance.run(use_reloader=True)

print(myList)
