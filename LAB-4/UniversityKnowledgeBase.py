# University Knowledge Base

# Knowledge Base containing information about students and courses

students = {
    "Anika": {
        "department": "MCA",
        "year": 4,
        "courses": ["Artificial Intelligence", "Data Structures"]
    },
    "Rahul": {
        "department": "MCA",
        "year": 3,
        "courses": ["Machine Learning", "Python"]
    },
    "Priya": {
        "department": "MBA",
        "year": 2,
        "courses": ["Marketing", "Finance"]
    }
}

# Display complete knowledge base
print("----- UNIVERSITY KNOWLEDGE BASE -----")

for name, details in students.items():
    print("\nStudent Name:", name)
    print("Department:", details["department"])
    print("Year:", details["year"])
    print("Courses:", ", ".join(details["courses"]))

# Query the knowledge base
search_student = input("\nEnter student name to search: ")

if search_student in students:
    print("\nStudent Found!")
    print("Name:", search_student)
    print("Department:", students[search_student]["department"])
    print("Year:", students[search_student]["year"])
    print("Courses:", ", ".join(students[search_student]["courses"]))
else:
    print("\nStudent not found in the Knowledge Base.")