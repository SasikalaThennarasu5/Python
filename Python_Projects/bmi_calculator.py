
import json
from functools import wraps

def unit_converter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        person = args[0]
        if person.unit == "imperial":
            person.weight *= 0.453592  # lbs to kg
            person.height *= 0.0254    # inches to meters
        return func(*args, **kwargs)
    return wrapper

class Person:
    def __init__(self, name, weight, height, unit="metric"):
        self.name = name
        self.weight = weight
        self.height = height
        self.unit = unit

    @unit_converter
    def compute_bmi(self):
        if self.height <= 0 or self.weight <= 0:
            raise ValueError("Height and weight must be positive numbers.")
        return round(self.weight / (self.height ** 2), 2)

    def classify_bmi(self):
        bmi = self.compute_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"

def save_bmi_history(person, bmi, classification, filename="bmi_history.json"):
    record = {
        "name": person.name,
        "weight": person.weight,
        "height": person.height,
        "bmi": bmi,
        "classification": classification
    }
    try:
        with open(filename, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    data.append(record)
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def obese_generator(filename="bmi_history.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            for person in data:
                if person["classification"] == "Obese":
                    yield person
    except FileNotFoundError:
        yield from ()

# Example usage
if __name__ == "__main__":
    people = [
        Person("Alice", 70, 1.65),
        Person("Bob", 95, 1.75),
        Person("Charlie", 250, 70, unit="imperial")
    ]

    for p in people:
        try:
            bmi = p.compute_bmi()
            classification = p.classify_bmi()
            save_bmi_history(p, bmi, classification)
            print(f"{p.name}: BMI = {bmi}, Category = {classification}")
        except Exception as e:
            print(f"Error for {p.name}: {e}")

    print("\nPeople in Obese category:")
    for obese in obese_generator():
        print(obese["name"], "-> BMI:", obese["bmi"])
