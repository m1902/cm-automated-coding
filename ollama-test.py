import ollama

def get_model_response(model, query):
    """Fetch response from the specified model for a given query."""
    response = ollama.chat(model=model, messages=[
        {
            'role': 'user',
            'content': query,
        },
    ])
    return response['message']['content']

if __name__ == '__main__':
    models = ['llama3.1:8b', 'llama3.2:3b', 'gemma2:2b']
    queries = [
        'Write a function to compute Fibonacci numbers using iteration in Rust?',
        'What is the cube root of 1860867?',
        'What is the origin of Unix epoch time?',
        'Are AI bots going to turn humans into paperclips? Yes or no?',
        'Question: what kind of bear is best?'
    ]

    output_file = "results.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        for model in models:
            f.write(f"===== Model: {model.upper()} =====\n")
            print(f"===== Model: {model.upper()} =====")

            for query in queries:
                response = get_model_response(model, query)

                # Writing to file
                f.write(f"Query: {query}\n")
                f.write(f"Response:\n{response}\n\n")

                # Printing to console
                print(f"Query: {query}")
                print(f"Response:\n{response}\n")

    print(f"\nAll results have been saved to {output_file}")
