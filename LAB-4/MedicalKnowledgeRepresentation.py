# Medical Knowledge Representation

# Knowledge base containing diseases and their symptoms

medical_knowledge = {
    "Common Cold": {
        "symptoms": ["Sneezing", "Runny Nose", "Sore Throat"],
        "treatment": "Rest and drink plenty of fluids"
    },
    "Flu": {
        "symptoms": ["Fever", "Cough", "Body Pain"],
        "treatment": "Rest, fluids, and consult a doctor if needed"
    },
    "Headache": {
        "symptoms": ["Head Pain", "Dizziness"],
        "treatment": "Rest and stay hydrated"
    }
}

print("----- MEDICAL KNOWLEDGE REPRESENTATION SYSTEM -----")

# Display the medical knowledge base
for disease, details in medical_knowledge.items():
    print("\nDisease:", disease)
    print("Symptoms:", ", ".join(details["symptoms"]))
    print("General Information:", details["treatment"])

# Search for a disease
search_disease = input("\nEnter a disease name to search: ")

if search_disease in medical_knowledge:
    print("\nDisease Found!")
    print("Disease:", search_disease)
    print("Symptoms:", ", ".join(medical_knowledge[search_disease]["symptoms"]))
    print("General Information:", medical_knowledge[search_disease]["treatment"])
else:
    print("\nDisease not found in the Knowledge Base.")