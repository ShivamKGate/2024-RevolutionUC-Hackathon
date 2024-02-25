from taipy import gui
import pandas as pd

# Read the data
data = pd.read_csv('C:\\Users\\skhar\\Downloads\\2024-RevolutionUC-Hackathon\\HealthSphere\\data1.csv')

# Define the number of bins for the histogram
nb_bins = 10

# Define the GUI page
page = f"""
Histogram
<|{data}|chart|type=histogram|>
"""

# Create the GUI instance and run it
gui_instance = gui.Gui(page)
gui_instance.run(use_reloader=True)
