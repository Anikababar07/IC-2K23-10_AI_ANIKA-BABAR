# Rule-Based Inference System

# Facts in the knowledge base
facts = {
    "has_fever": True,
    "has_cough": True,
    "has_headache": False
}

def infer_disease(facts):
    if facts["has_fever"] and facts["has_cough"]:
        return "Possible Flu"

    elif facts["has_headache"]:
        return "Possible Headache"

    else:
        return "No conclusion can be made"


print("----- RULE-BASED INFERENCE SYSTEM -----")

print("\nFacts:")
for fact, value in facts.items():
    print(fact, ":", value)

result = infer_disease(facts)

print("\nInference Result:", result)