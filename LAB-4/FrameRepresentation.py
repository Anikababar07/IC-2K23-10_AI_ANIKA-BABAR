# Frame Representation in Artificial Intelligence

# Creating a frame for a student

student_frame = {
    "Name": "Anika",
    "Age": 23,
    "Course": "MCA",
    "College": "IIPS DAVV",
    "Year": 4
}

print("----- STUDENT FRAME REPRESENTATION -----")

# Display frame information
for slot, value in student_frame.items():
    print(slot + ":", value)

# Search for a specific slot
search_slot = input("\nEnter a slot name to search (Name, Age, Course, College, Year): ")

if search_slot in student_frame:
    print(search_slot + ":", student_frame[search_slot])
else:
    print("Slot not found in the frame.")