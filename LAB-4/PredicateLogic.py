# Predicate Logic in Artificial Intelligence

# Knowledge base
students = ["Anika", "Rahul", "Priya"]

def is_student(person):
    return person in students

def is_mca_student(person):
    return is_student(person)

print("----- PREDICATE LOGIC -----")

person = input("Enter a name: ")

if is_student(person):
    print(person, "is a Student.")

    if is_mca_student(person):
        print(person, "is an MCA Student.")
else:
    print(person, "is not found in the Student Knowledge Base.")