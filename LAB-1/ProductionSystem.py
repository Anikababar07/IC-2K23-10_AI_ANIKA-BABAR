def rule_based_system(symptoms):
    if "fever" in symptoms and "cough" in symptoms:
        return "Possible Flu"
    elif "headache" in symptoms and "stress" in symptoms:
        return "Possible Stress"
    elif "stomach_pain" in symptoms:
        return "Possible Stomach Problem"
    else:
        return "No matching rule found"


print("Simple Rule-Based Production System")

user_input = input(
    "Enter symptoms separated by commas (fever, cough, headache, stress, stomach_pain): "
)

symptoms = [symptom.strip().lower() for symptom in user_input.split(",")]

result = rule_based_system(symptoms)

print("Result:", result)