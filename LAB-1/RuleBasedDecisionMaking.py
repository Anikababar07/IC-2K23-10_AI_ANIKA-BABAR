# Rule-Based Decision Making System

def make_decision(weather):
    if weather == "Rainy":
        return "Take an umbrella"
    
    elif weather == "Sunny":
        return "Wear sunglasses"
    
    elif weather == "Cold":
        return "Wear a jacket"
    
    else:
        return "No specific decision"


# Input from the user
weather = input("Enter the weather (Rainy/Sunny/Cold): ")

# Display the decision
decision = make_decision(weather)
print("Decision:", decision)