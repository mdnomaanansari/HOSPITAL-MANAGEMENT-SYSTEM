SMARTCARE HOSPITAL SYSTEM

A lightweight, console-based hospital management application written in Python. This system allows hospital staff to manage patient admissions, prioritize treatments using a severity-based triage queue, and generate automated billing invoices upon discharge.

FEATURES

* Patient Admission: Captures patient details (name, age, blood group, contact, disease) and a severity score (1-5).
* Smart Allocation: Automatically assigns rooms based on the patient's severity (ICU for critical, Private Room for moderate, General Ward for low severity). Randomly assigns an available doctor.
* Triage Queue: Displays all currently admitted patients, automatically sorted by severity (highest to lowest) so critical patients are treated first.
* Search Functionality: Quickly find active patient records by searching for their name or diagnosis.
* Doctor Roster: View a list of all currently available doctors on duty.
* Automated Billing & Discharge: Generates a detailed tax invoice upon patient discharge, calculating base fees, doctor fees, room charges, medication costs (scaled by severity), and an 18% GST.
* Data Persistence: Automatically saves active patient records to a local JSON file (hospital_db.json), ensuring no data is lost between sessions.

PREREQUISITES

* Python 3.x: This script relies solely on Python's standard libraries (os, json, random). No external dependencies or pip installations are required.

INSTALLATION & EXECUTION

1. Save the provided Python script to a file, for example: smartcare.py.
2. Open your terminal or command prompt.
3. Navigate to the directory where the file is saved.
4. Run the script using the following command:
python smartcare.py

MENU OPTIONS GUIDE

When you run the application, you will be presented with a 6-option menu:

1. Admit New Patient: Follow the prompts to enter the patient's details. Severity must be an integer from 1 (Low) to 5 (Critical).
2. View Patient Triage Queue: Displays a tabular view of all admitted patients, prioritized by their medical severity.
3. Search by Disease or Name: Enter a partial or full string to find matching patient profiles.
4. View Available Doctors: Lists the doctors currently available for random assignment.
5. Discharge & Generate Invoice: Type the exact name of an admitted patient to remove them from the active queue and print their final hospital bill.
6. Save Data & Quit: Safely writes all current queues to hospital_db.json and exits the program.

TECHNICAL DETAILS

* Database: The application creates and manages a file named hospital_db.json in the same directory as the script. Deleting this file will reset the hospital database.
* Sorting Algorithm: The triage queue utilizes a bubble sort algorithm to continuously order the queue in descending order of severity.
