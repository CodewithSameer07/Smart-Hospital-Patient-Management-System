"""Smart Hospital Patient Management System."""
import math
RISK_PRIORITY = {
    "Normal": 1,
    "Critical": 2,
    "Emergency": 3,
}
# This function takes patient information from the user.
def get_patient_data():
    while True:
        name = input("Enter patient name: ").strip()  # Take the patient's name
        # Check that the name is not empty.
        if name:
            break
        # Display an error message when the name is empty.
        print("Patient name cannot be empty. Please try again.")
    # This loop is used to validate the patient's age.
    while True:
        # Try to convert the entered age into an integer.
        try:
            age = int(input("Enter patient age: "))
            # Check that the age is within a reasonable range.
            if 0 <= age <= 120:
                break
            # Display an error when the age is outside the valid range.
            print("Age must be between 0 and 120.")
        # Handle the error if the user enters something other than a number.
        except ValueError:
            print("Please enter a valid whole number for age.")
    # This loop is used to validate body temperature.
    while True:
        # Try to convert the temperature into a floating-point number.
        try:
            temperature = float(input("Enter body temperature (°F): "))
            # Check that the temperature is within a reasonable range.
            if math.isfinite(temperature) and 80 <= temperature <= 115:
                break
            # Display an error when the temperature is invalid.
            print("Temperature must be between 80°F and 115°F.")
        # Handle invalid temperature input.
        except ValueError:
            print("Please enter a valid number for temperature.")
    # This loop is used to validate oxygen level.
    while True:
        # Try to convert oxygen level into a floating-point number.
        try:
            oxygen = float(input("Enter oxygen level (%): "))
            # Check that oxygen level is between 0 and 100 percent.
            if math.isfinite(oxygen) and 0 <= oxygen <= 100:
                break
            # Display an error when oxygen level is outside the valid range.
            print("Oxygen level must be between 0% and 100%.")
        # Handle invalid oxygen input.
        except ValueError:
            print("Please enter a valid number for oxygen level.")
    # Return all patient information in a dictionary.
    return {
        "name": name,
        "age": age,
        "temperature": temperature,
        "oxygen": oxygen
    }
# This function classifies a patient according to the given health conditions.
def classify_patient(patient):
    # Get the patient's temperature from the dictionary.
    temperature = patient["temperature"]
    # Get the patient's oxygen level from the dictionary.
    oxygen = patient["oxygen"]
    # Emergency has the highest priority, so it is checked first.
    if oxygen < 85 or temperature >= 103:
        return "Emergency"
    # Critical conditions are checked after Emergency conditions.
    elif 85 <= oxygen <= 92 or 100 <= temperature < 103:
        return "Critical"
    # If no critical or emergency condition is found, the patient is normal.
    else:
        return "Normal"
# This function adds a patient record to the patient list.
def add_patient(patients):
    # Get the patient's information from the input function.
    patient = get_patient_data()
    # Classify the patient according to the health conditions.
    patient["category"] = classify_patient(patient)
    # Add the complete patient record to the list.
    patients.append(patient)
    # Display confirmation after successfully adding the record.
    print("\nPatient record added successfully.")
    # Display the patient's risk category.
    print("Risk Category:", patient["category"])
# This function calculates and displays average health values.
def calculate_averages(patients):
    # Check whether there are any patient records.
    if not patients:
        print("\nNo patient records available.")
        return
    # Add all patient temperatures together.
    total_temperature = sum(patient["temperature"] for patient in patients)
    # Add all patient oxygen levels together.
    total_oxygen = sum(patient["oxygen"] for patient in patients)
    # Calculate the average temperature.
    average_temperature = total_temperature / len(patients)
    # Calculate the average oxygen level.
    average_oxygen = total_oxygen / len(patients)
    # Display the calculated average temperature.
    print("\nAverage Temperature:", round(average_temperature, 2), "°F")

    # Display the calculated average oxygen level.
    print("Average Oxygen Level:", round(average_oxygen, 2), "%")
    return average_temperature, average_oxygen
# This function displays all stored patient records.
def display_patients(patients):
    # Check whether the patient list is empty.
    if not patients:
        print("\nNo patient records available.")
        return
    # Display a heading before showing the records.
    print("\n========== PATIENT RECORDS ==========")
    # Use a loop to display every patient record.
    for number, patient in enumerate(patients, start=1):
        # Display the patient's record number.
        print("\nPatient", number)
        # Display the patient's name.
        print("Name:", patient["name"])
        # Display the patient's age.
        print("Age:", patient["age"])
        # Display the patient's body temperature.
        print("Temperature:", patient["temperature"], "°F")
        # Display the patient's oxygen level.
        print("Oxygen Level:", patient["oxygen"], "%")
        # Display the patient's risk category.
        print("Category:", patient["category"])
# This function finds and displays the highest-risk patient.
def highest_risk_patient(patients):
    # Check whether any records exist.
    if not patients:
        print("\nNo patient records available.")
        return
    # Define the priority of each patient category.
    # Start with the first patient as the highest-risk patient.
    highest_patient = patients[0]
    # Check all remaining patients using a loop.
    for patient in patients:
        # Compare the current patient's category priority with the highest risk.
        if (
            RISK_PRIORITY[patient["category"]]
            > RISK_PRIORITY[highest_patient["category"]]
        ):
            # Update the highest-risk patient when a higher category is found.
            highest_patient = patient
    # Display the highest-risk patient's information.
    print("\n========== HIGHEST-RISK PATIENT ==========")
    # Display the patient's name.
    print("Name:", highest_patient["name"])
    # Display the patient's age.
    print("Age:", highest_patient["age"])
    # Display the patient's temperature.
    print("Temperature:", highest_patient["temperature"], "°F")
    # Display the patient's oxygen level.
    print("Oxygen Level:", highest_patient["oxygen"], "%")
    # Display the patient's category.
    print("Category:", highest_patient["category"])
    return highest_patient
# This function counts patients according to their risk categories.
def display_risk_summary(patients):
    # Check whether any patient records exist.
    if not patients:
        print("\nNo patient records available.")
        return
    # Create counters for each category.
    normal_count = 0
    critical_count = 0
    emergency_count = 0
    # Loop through all patient records.
    for patient in patients:
        # Increase the normal counter when the category is Normal.
        if patient["category"] == "Normal":
            normal_count += 1
        # Increase the critical counter when the category is Critical.
        elif patient["category"] == "Critical":
            critical_count += 1
        # Increase the emergency counter when the category is Emergency.
        elif patient["category"] == "Emergency":
            emergency_count += 1
    # Display the total number of critical patients.
    print("\nTotal Critical Patients:", critical_count)
    # Display the total number of emergency patients.
    print("Total Emergency Patients:", emergency_count)
    # Display the total number of normal patients.
    print("Normal Patients Count:", normal_count)
    return {
        "Normal": normal_count,
        "Critical": critical_count,
        "Emergency": emergency_count,
    }
# This function displays the main menu of the hospital system.
def display_menu():
    # Display the system title.
    print("\n========================================")
    # Display the name of the application.
    print(" SMART HOSPITAL PATIENT MANAGEMENT SYSTEM")
    # Display the bottom border of the title.
    print("========================================")
    # Display menu option 1.
    print("1. Add Patient")
    # Display menu option 2.
    print("2. Display Patient Records")
    # Display menu option 3.
    print("3. Calculate Average Temperature and Oxygen")
    # Display menu option 4.
    print("4. Display Risk Summary")
    # Display menu option 5.
    print("5. Display Highest-Risk Patient")
    # Display menu option 6.
    print("6. Exit")
# This is the main function that controls the complete application.
def main():
    # Create an empty list to store multiple patient records.
    patients = []
    # Start an infinite loop for the menu-driven system.
    while True:
        # Display the available menu options.
        display_menu()
        # Take the user's menu choice.
        choice = input("\nEnter your choice (1-6): ").strip()
        # Add a new patient when the user selects option 1.
        if choice == "1":
            add_patient(patients)
        # Display all patient records when option 2 is selected.
        elif choice == "2":
            display_patients(patients)
        # Calculate averages when option 3 is selected.
        elif choice == "3":
            calculate_averages(patients)
        # Display category counts when option 4 is selected.
        elif choice == "4":
            display_risk_summary(patients)
        # Display the highest-risk patient when option 5 is selected.
        elif choice == "5":
            highest_risk_patient(patients)
        # Exit the program when option 6 is selected.
        elif choice == "6":
            print("\nThank you for using the Smart Hospital System.")
            break
        # Handle an invalid menu choice.
        else:
            print("\nInvalid choice. Please select a number from 1 to 6.")
# This condition makes sure the main function runs when this file is executed.
if __name__ == "__main__":
    # Start the Smart Hospital Patient Management System.
    main()