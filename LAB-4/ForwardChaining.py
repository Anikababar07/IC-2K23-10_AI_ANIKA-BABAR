# Forward Chaining in Artificial Intelligence

# Initial facts
facts = ["fever", "cough"]

# Rules
rules = {
    ("fever", "cough"): "flu",
    ("flu",): "needs_rest"
}

# Store all known facts
known_facts = facts.copy()

print("----- FORWARD CHAINING -----")
print("\nInitial Facts:", known_facts)

changed = True

while changed:
    changed = False

    for conditions, conclusion in rules.items():
        # Check if all conditions of a rule are true
        if all(condition in known_facts for condition in conditions):
            if conclusion not in known_facts:
                known_facts.append(conclusion)
                print("New conclusion:", conclusion)
                changed = True

print("\nFinal Knowledge:", known_facts)