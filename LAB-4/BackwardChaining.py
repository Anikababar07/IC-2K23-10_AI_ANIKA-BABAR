# Backward Chaining in Artificial Intelligence

# Known facts
facts = ["fever", "cough"]

# Rules
rules = {
    "flu": ["fever", "cough"],
    "needs_rest": ["flu"]
}


def backward_chain(goal):
    # Check if the goal is already a known fact
    if goal in facts:
        return True

    # Check if there is a rule for the goal
    if goal in rules:
        conditions = rules[goal]

        # Check whether all conditions can be proved
        for condition in conditions:
            if not backward_chain(condition):
                return False

        return True

    return False


print("----- BACKWARD CHAINING -----")
print("\nKnown Facts:", facts)

goal = input("\nEnter a goal to prove (flu/needs_rest): ")

if backward_chain(goal):
    print("\nGoal '" + goal + "' can be proved!")
else:
    print("\nGoal '" + goal + "' cannot be proved.")