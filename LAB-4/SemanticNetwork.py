# Semantic Network Construction

# A semantic network representing relationships between concepts

semantic_network = {
    "Student": ["is a Person", "studies at University"],
    "Teacher": ["is a Person", "teaches Students"],
    "University": ["has Students", "has Teachers"],
    "Anika": ["is a Student", "studies at IIPS"],
    "IIPS": ["is a University"]
}

print("----- SEMANTIC NETWORK -----")

# Display the semantic network
for concept, relationships in semantic_network.items():
    print("\nConcept:", concept)
    for relationship in relationships:
        print(" ->", relationship)

# Search for a concept
search_concept = input("\nEnter a concept to search: ")

if search_concept in semantic_network:
    print("\nConcept Found!")
    print("Relationships of", search_concept + ":")
    for relationship in semantic_network[search_concept]:
        print(" ->", relationship)
else:
    print("\nConcept not found in the Semantic Network.")