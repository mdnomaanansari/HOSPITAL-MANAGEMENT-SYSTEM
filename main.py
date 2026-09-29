import os
import json
import random

db_file = 'hospital_db.json'
q = []
dox = ['Dr. Sharma ', 'Dr. Verma ', 'Dr. Gupta ', 'Dr. Ali ']

if os.path.exists(db_file):
    f = open(db_file, 'r')
    content = f.read()
    if len(content) > 0:
        q = json.loads(content)
    f.close()

while 1:
    print("\n" + "="*35)
    print("      SMARTCARE HOSPITAL SYSTEM")
    print("="*35)
    print("1. Admit New Patient")
    print("2. View Patient Triage Queue")
    print("3. Search by Disease or Name")
    print("4. View Available Doctors")
    print("5. Discharge & Generate Invoice")
    print("6. Exit")  
    print("="*35)
    
    opt = input("Select an option (1-6): ")

    if opt == '1':
        print("\n--- ENTER PATIENT DETAILS ---")
        nm = input("Patient Name: ")
        ag = input("Age: ")
        bg = input("Blood Group: ")
        ph = input("Phone Number: ")
        dz = input("Disease/Symptom: ")
        sv = input("Severity (1=Low to 5=Critical): ")
        
        s_val = 1
        if sv == '2': s_val = 2
        if sv == '3': s_val = 3
        if sv == '4': s_val = 4
        if sv == '5': s_val = 5
                
        r_type = 'General Ward'
        if s_val > 3:
            r_type = 'ICU'
        elif s_val == 3:
            r_type = 'Private Room'
            
        doc_assigned = random.choice(dox)
        
        new_patient = {
            'name': nm,
            'age': ag,
            'bgroup': bg,
            'phone': ph,
            'disease': dz,
            'sev': s_val,
            'doc': doc_assigned,
            'room': r_type
        }
        
        q.append(new_patient)
        print("\n[SUCCESS] Patient Admitted Successfully.")
        print("Assigned Doctor: " + doc_assigned)
        print("Allotted Room: " + r_type)
        
        input("\nPress Enter to return to menu...")

    elif opt == "2":
        print("\n--- PATIENT TRIAGE QUEUE ---")
        if len(q) == 0:
            print("Hospital queue is currently empty.")
        else:
            is_sorted = 0
            while is_sorted == 0:
                is_sorted = 1
                idx = 0
                while idx < len(q) - 1:
                    if q[idx]['sev'] < q[idx+1]['sev']:
                        temp_val = q[idx]
                        q[idx] = q[idx+1]
                        q[idx+1] = temp_val
                        is_sorted = 0
                    idx = idx + 1
                        
            print("Name          | Age | Sev | Room      | Doctor")
            print("-" * 55)
            for p in q:
                print(p['name'] + " | " + p['age'] + "  | " + str(p['sev']) + "   | " + p['room'] + " | " + p['doc'])
                
        input("\nPress Enter to return to menu...")

    elif opt == '3':
        print("\n--- SEARCH DATABASE ---")
        term = input("Enter disease or patient name to search: ")
        fnd = 0
        for pt in q:
            if term.lower() in pt['disease'].lower() or term.lower() in pt['name'].lower():
                print("\n[Record Found]")
                print("Name: " + pt['name'] + " (Contact: " + pt['phone'] + ")")
                print("Age: " + pt['age'] + " | Blood Group: " + pt['bgroup'])
                print("Diagnosis: " + pt['disease'])
                print("Treating Doctor: " + pt['doc'] + " in " + pt['room'])
                fnd = 1
                
        if fnd == 0:
            print("No matching records found in the database.")
            
        input("\nPress Enter to return to menu...")
        
    elif opt == '4':
        print("\n--- AVAILABLE DOCTORS LIST ---")
        d_count = 1
        for d in dox:
            print(str(d_count) + ". " + d)
            d_count = d_count + 1
            
        input("\nPress Enter to return to menu...")

    elif opt == '5':
        print("\n--- DISCHARGE & BILLING ---")
        d_nm = input("Enter exact Patient Name to discharge: ")
        i = 0
        found_dis = 0
        
        while i < len(q):
            if q[i]['name'] == d_nm:
                found_dis = 1
                
                base_charge = 500
                doc_charge = 800
                
                room_charge = 1000
                if q[i]['room'] == 'ICU':
                    room_charge = 5000
                elif q[i]['room'] == 'Private Room':
                    room_charge = 2500
                    
                med_charge = q[i]['sev'] * 450
                total_b = base_charge + doc_charge + room_charge + med_charge
                tax = total_b * 0.18
                
                print("\n" + "*"*35)
                print("      SMARTCARE TAX INVOICE")
                print("*"*35)
                print("Patient Name  : " + q[i]['name'])
                print("Age & Blood   : " + q[i]['age'] + " | " + q[i]['bgroup'])
                print("Diagnosis     : " + q[i]['disease'])
                print("Consultant    : " + q[i]['doc'])
                print("-" * 35)
                print("Base Reg. Fee : Rs. " + str(base_charge))
                print("Doctor Visit  : Rs. " + str(doc_charge))
                print("Room Charge   : Rs. " + str(room_charge) + " (" + q[i]['room'] + ")")
                print("Medications   : Rs. " + str(med_charge))
                print("GST (18%)     : Rs. " + str(tax))
                print("-" * 35)
                print("GRAND TOTAL   : Rs. " + str(total_b + tax))
                print("*"*35)
                
                q.pop(i)
                print("\nPatient successfully discharged from the system.")
                break
            i = i + 1
            
        if found_dis == 0:
            print("Error: Patient not found in the active records.")
            
        input("\nPress Enter to return to menu...")

    elif opt == '6':
        print("\nSystem Shutting Down. Goodbye!")
        break
        
    else:
        print("\nInvalid input. Please try again.")
        input("Press Enter to return to menu...")
