# Logical Rule Engine

# Facts
facts = {
    "fever": True,
    "cough": True,
    "body_pain": True
}

# Rules
rules = [
    {
        "conditions": ["fever", "cough"],
        "conclusion": "flu"
    },
    {
        "conditions": ["flu", "body_pain"],
        "conclusion": "severe_flu"
    }
]

# Forward Chaining Rule Engine
def logical_rule_engine(facts, rules):
    inferred_facts = facts.copy()
    changed = True

    while changed:
        changed = False

        for rule in rules:
            conditions_met = all(
                inferred_facts.get(condition, False)
                for condition in rule["conditions"]
            )

            conclusion = rule["conclusion"]

            if conditions_met and conclusion not in inferred_facts:
                inferred_facts[conclusion] = True
                print(f"Rule Applied: {rule['conditions']} -> {conclusion}")
                changed = True

    return inferred_facts


# Run the Logical Rule Engine
result = logical_rule_engine(facts, rules)

print("\nFinal Inferred Facts:")
for fact, value in result.items():
    if value:
        print("-", fact)