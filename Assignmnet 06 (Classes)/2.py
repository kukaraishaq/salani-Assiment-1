from datetime import datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = namegit push -u origin master:main

        self.country = country
        # Store date of birth as a datetime object
        self.date_of_birth = datetime.strptime(date_of_birth, "%d/%m/%Y")

    def calculate_age(self):
        today = datetime.today()
        age = today.year - self.date_of_birth.year
        # Adjust if birthday hasn't occurred yet this year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age


# Example usage
name = input("Enter name: ")
country = input("Enter country: ")
dob = input("Enter date of birth (dd/mm/yyyy): ")

p = Person(name, country, dob)

print(f"\nName: {p.name}")
print(f"Country: {p.country}")
print(f"Date of Birth: {p.date_of_birth.strftime('%d %B %Y')}")
print(f"Age: {p.calculate_age()} years")
