SmartCare Hospital System

A simple, command-line Python application designed to manage basic hospital operations, including patient admission, triage prioritization, searching, and automated billing.

FEATURES

Admit New Patients: Captures patient details (name, age, blood group, phone, disease, and severity). Automatically assigns a room type (General Ward, Private Room, or ICU) based on the severity of the condition and randomly assigns an available doctor.

Patient Triage Queue: Displays a list of all currently admitted patients sorted by severity (highest to lowest) to ensure critical patients are prioritized.

Search Database: Allows staff to quickly look up active patient records by searching for their name or diagnosed disease.

View Available Doctors: Displays the current roster of on-call doctors.

Discharge & Billing: Generates a detailed, itemized tax invoice upon discharge. Calculates base fees, doctor visitation fees, room charges, medication costs (scaled by severity), and an 18% GST. Discharging a patient automatically removes them from the active hospital queue.

PREREQUISITES

Python 3.x: This script uses standard Python libraries (os, json, random). No external dependencies or packages are required.

HOW TO RUN

1. Save the provided Python code into a file, for example: smartcare.py.
2. Open your terminal or command prompt.
3. Navigate to the directory where you saved the file.
4. Run the script using the following command: python smartcare.py

USAGE MENU

Upon running the script, you will be presented with a looping main menu. Enter a number between 1 and 6 to interact with the system:

1. Admit New Patient: Follow the prompts to enter patient details. Severity should be an integer from 1 (Low) to 5 (Critical).
2. View Patient Triage Queue: Prints a table of patients. It uses a custom sorting algorithm to bring patients with the highest severity score to the top of the list.
3. Search by Disease or Name: Enter a keyword to find specific patients.
4. View Available Doctors: Lists the doctors hardcoded in the system (Dr. Sharma, Dr. Verma, Dr. Gupta, Dr. Ali).
5. Discharge & Generate Invoice: Enter the exact name of the patient to generate their final bill and remove them from the system.
6. Exit: Safely shuts down the application.
