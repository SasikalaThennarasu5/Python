# healthcare_records.py

def add_patient_record(records_db, patient_id, name, illnesses):
    """Add a patient record with ID as tuple and illnesses as a set."""
    patient_key = (patient_id,)  # Tuple for immutability
    records_db[patient_key] = {
        'name': name,
        'illnesses': set(illnesses)
    }
    print(f"Added record for patient {name} (ID: {patient_id})")


def update_illness(records_db, patient_id, new_illness):
    """Add a new illness to an existing patient."""
    patient_key = (patient_id,)
    if patient_key in records_db:
        records_db[patient_key]['illnesses'].add(new_illness)
        print(f"Updated illnesses for patient ID {patient_id}.")
    else:
        print(f"No record found for patient ID {patient_id}.")


def show_all_records(records_db):
    """Display all patient records."""
    print("\nMedical Records:")
    for patient_key, data in records_db.items():
        print(f"Patient ID: {patient_key[0]}")
        print(f"Name: {data['name']}")
        print(f"Illnesses: {data['illnesses']}")
        print("-" * 40)
