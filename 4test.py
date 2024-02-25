from taipy import Gui
import pandas as pd

# Load the data
data = pd.read_csv('C:\\Users\\skhar\\Downloads\\2024-RevolutionUC-Hackathon\\HealthSphere\\data2.csv')

# Count the occurrences of each unique condition
status_counts_updated = data['Condition'].value_counts()
print(status_counts_updated)

my_data = {
    "Condition": status_counts_updated.index.tolist(),
    "Count": status_counts_updated.values.tolist()
}

options = {
    # Fill to x axis
    "fill": "tozeroy"
}
# Define the GUI page to include a pie chart based on 'Condition' and 'Phase'
page = """
# Phase vs Condition
<|{my_data}|chart|x=Count|y=Condition|options={options}|>
"""

# Initialize and run the GUI instance
gui_instance = Gui(page)
gui_instance.run(use_reloader=False)  # Set 'use_reloader' to False for simplicity in this example
