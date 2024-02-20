# import random

# # Define patterns and responses
# patterns = {
#     "hi": ["Hello!", "Hi there!", "Hey!"],
#     "how are you": ["I'm doing well, thanks for asking!", "I'm good, how about you?"],
#     "bye": ["Goodbye!", "See you later!", "Bye!"]
# }

# # Function to generate response
# def get_response(user_input):
#     for pattern, responses in patterns.items():
#         if pattern in user_input.lower():
#             return random.choice(responses)
#     return "I'm sorry, I didn't understand that."

# # Main loop
# while True:
#     user_input = input("You: ")
#     if user_input.lower() == 'quit':
#         print("Chatbot: Goodbye!")
#         break
#     response = get_response(user_input)
#     print("Chatbot:", response)

# ---------------------------------------------------------------------------------------------

# import random

# # Function to read questions and answers from a file
# def read_qa_file(filename):
#     qa_dict = {}
#     with open(filename, 'r') as file:
#         for line in file:
#             parts = line.strip().split(',', 1)  # Split at the first comma
#             if len(parts) == 2:
#                 question, answer = parts
#                 qa_dict[question.lower()] = answer
#             else:
#                 print("Invalid line in file:", line)
#     return qa_dict


# # Function to generate response
# def get_response(user_input, qa_dict):
#     for question, answer in qa_dict.items():
#         if question in user_input.lower():
#             return answer
#     return "I'm sorry, I didn't understand that."

# # Main function
# def main():
#     qa_dict = read_qa_file(r"C:\Users\SUBHASH NIRMAL\Desktop\pyFile.txt")

#     # Main loop
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() == 'quit':
#             print("Chatbot: Goodbye!")
#             break
#         response = get_response(user_input, qa_dict)
#         print("Chatbot:", response)

# if __name__ == "__main__":
#     main()

# -----------------------------------------------------------------------------------------------
from fuzzywuzzy import fuzz

# Function to read questions and answers from a file
def read_qa_file(filename):
    qa_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',', 1)  # Split at the first comma
            if len(parts) == 2:
                question, answer = parts
                qa_dict[question.lower()] = answer
            else:
                print("Invalid line in file:", line)
    return qa_dict

# Function to generate response using fuzzy string matching
def get_response(user_input, qa_dict):
    max_score = 0
    best_question = None
    for question in qa_dict.keys():
        score = fuzz.ratio(user_input.lower(), question)
        if score > max_score:
            max_score = score
            best_question = question

    if max_score >= 70:  # Adjust the threshold as needed
        return qa_dict[best_question]
    else:
        return "I'm sorry, I didn't understand that."

# Main function
def main():
    qa_dict = read_qa_file(r"C:\Users\SUBHASH NIRMAL\Desktop\pyFile\pyFile.txt")
    # Main loop
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input, qa_dict)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
