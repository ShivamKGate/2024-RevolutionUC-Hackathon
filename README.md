This is the Revolution UC 2024 Hackathon Project from Team Kartavya & Shivam. 
The Project is called HealthSphere: - Data-Driven Wellness Solution

To Get Started with this project: 

Windows:
    Pre-requisites: 
        Python 3.8+ & Python 3.11-
        Requirements.txt file from the directory

    Steps:
    1. To Activate the Flask-Python Backend
        You would need to be in the right directory of 2024-RevolutionUC-Hackathon/HealthSphere: 
        So if you aren't here already you can type : 
        'cd 2024-RevolutionUC-Hackathon/HealthSphere'

        or 

        "cd HealthSphere"

        once you are at the root of the project

        to download the required libraries for the virtual environment use the following command:

        "pip install -r requirements.txt"

        create a virtual environment using the following command: 

        "python -m venv venv"

        activate the virtual environment using the following command:

        "venv/Scripts/activate"

        to deactivate the virtual environment use the following command:

        "deactivate" (optional)

        to download the required libraries for the virtual environment use the following command:

        "pip install -r requirements.txt"

        to run the project use the following command:

        "python app.py"

    2. To Launch the Taipy Dashboard use the following command
        2.1 create another Terminal
        2.2 python taipyserver.py

        launch it on http://127.0.0.1:8080


Mac:
    For macOS, the steps are quite similar to those for Windows, but there are a few differences. Here are the instructions for setting up and running the HealthSphere project on macOS:

Pre-requisites:
Python 3.8+ & Python 3.11-
Requirements.txt file from the project directory
Terminal application
Steps:
Open Terminal:
Open the Terminal application on your macOS. You can find it by searching for "Terminal" in Spotlight or navigating to Applications > Utilities > Terminal.

Navigate to Project Directory:
Use the cd command to navigate to the root directory of your HealthSphere project. If the project is located in your home directory, you can use:

javascript
Copy code
cd ~/2024-RevolutionUC-Hackathon/HealthSphere
If it's located elsewhere, navigate to the appropriate directory.

Setup Virtual Environment:
Run the following commands in Terminal to set up a virtual environment and activate it:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install Dependencies:
Once the virtual environment is activated, install the required Python libraries using pip:

Copy code
pip install -r requirements.txt
Run Flask Backend:
Start the Flask backend server by running:

Copy code
python app.py
Launch Taipy Dashboard:
Open another Terminal window (or tab) and navigate to the project directory if you're not already there.

Then, run the Taipy Dashboard server using:

Copy code
python taipyserver.py
Access the Application:
Once both the Flask backend and Taipy Dashboard are running, you can access the HealthSphere application by visiting http://127.0.0.1:8080 in your web browser.
