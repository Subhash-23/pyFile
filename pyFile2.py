import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to read input paragraph from a file
def read_input_paragraph(filename):
    with open(filename, 'r') as file:
        paragraph = file.read()
    return paragraph

# Function to preprocess text
def preprocess_text(text):
    tokens = nltk.word_tokenize(text.lower())
    return ' '.join(tokens)

# Function to generate response based on user's question
def generate_response(question, paragraph):
    # Tokenize and preprocess the input paragraph
    sentences = nltk.sent_tokenize(paragraph)
    preprocessed_sentences = [preprocess_text(sentence) for sentence in sentences]
    
    # Preprocess the user's question
    preprocessed_question = preprocess_text(question)
    
    # Calculate TF-IDF vectors
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([preprocessed_question] + preprocessed_sentences)
    
    # Calculate cosine similarity between the question and each sentence
    similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])[0]
    
    # Find the index of the sentence with the highest similarity score
    max_index = similarity_scores.argmax()
    
    # Return the corresponding sentence as the answer
    return sentences[max_index]

# Main function
def main():
    # Read input paragraph from file
    paragraph = read_input_paragraph(r"C:\Users\SUBHASH NIRMAL\Desktop\pyFile\pyFile2.txt")

    # Main loop
    while True:
        user_question = input("You: ")
        if user_question.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        response = generate_response(user_question, paragraph)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
