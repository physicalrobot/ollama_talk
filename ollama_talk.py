import ollama

# Initialize the model and context
model_name = "llama3.2"
context = {"prompt": ""}

def get_response(user_input):
    global context
    
    # Add the user input to the prompt
    if not context["prompt"]:
        context["prompt"] = "User: " + user_input
    else:
        context["prompt"] += " \nUser: " + user_input

    # Use the ollama API to generate a response
    generated_dict = ollama.generate(model=model_name, prompt=context["prompt"])

    # Access the 'response' key from the dictionary to get the generated text
    generated_text = generated_dict.get('response', '')

    # Update the prompt by appending the model's response for continuity
    context["prompt"] += "\nZaku69: " + generated_text

    return generated_text

def chat_loop():
    while True:
        # Get user input for the next prompt
        response = input("\033[1;32mUser: \033[0m")
        
        # Exit the loop if no response is given
        if not response:
            break

        # Get response from the model
        user_input = get_response(response)
        
        # Ensure user_input is a string before printing
        print("\033[91mZaku69: \033[0m" + user_input)

chat_loop()
