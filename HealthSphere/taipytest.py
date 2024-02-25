from taipy import gui
import pandas as pd

nb_points = 10000
data = pd.read_csv('C:\\Users\\skhar\\Downloads\\2024-RevolutionUC-Hackathon\\HealthSphere\\data.csv')
page = """
#Years vs Enrollment
<|{nb_points}|slider|min=10000|max=15000|>
<|{data[:nb_points]}|chart|min=1980|max=2025|>
"""

# Correcting the usage of the `gui` module
gui_instance = gui.Gui(page)
gui_instance.run(use_reloader=True)
