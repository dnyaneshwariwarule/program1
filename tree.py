def decision_tree(node):
    if isinstance(node, dict):
        
        question = next(iter(node))
        answer = input(question + " (Yes/No): ").strip().capitalize()
        
        
        if answer in node[question]:
           
            return decision_tree(node[question][answer])
        else:
            print("Invalid answer. Please respond with 'Yes' or 'No'.")
            return decision_tree(node)
    else:
       
        return node

# Knowledge base
K_Base = {
    "Is the computer powering on?": {
        "Yes": {
            "Is there a beeping sound?": {
                "Yes": "Check the RAM and CPU",
                "No": {
                    "Is the display showing any output?": {
                        "Yes": "Check the display connections and settings",
                        "No": "Check the power supply and motherboard"
                    }
                }
            }
        },
        "No": "Check the power supply and cables"
    }
}

# Start the decision tree
result = decision_tree(K_Base)
print("\nAdvice:", result)
