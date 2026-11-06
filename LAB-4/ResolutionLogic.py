# Resolution in Propositional Logic

# Clause 1: P OR Q
clause1 = {"P", "Q"}

# Clause 2: NOT P
clause2 = {"NOT P"}

print("----- RESOLUTION IN PROPOSITIONAL LOGIC -----")

print("\nClause 1:", clause1)
print("Clause 2:", clause2)

# Simple resolution demonstration
if "P" in clause1 and "NOT P" in clause2:
    # Remove P and NOT P to get the remaining literal
    resolvent = clause1 - {"P"}

    print("\nResolving P and NOT P...")
    print("Resolvent:", resolvent)
else:
    print("\nNo resolution possible.")