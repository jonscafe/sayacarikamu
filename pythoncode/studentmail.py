from googlesearch import search

def google_search(query, num_results=5):
    results = [result for result in search(query, num_results=num_results)]
    return results

def run_studentmail_search(user_input):
    print('STUDENTMAIL SEARCH (GOOGLE DORKING)')
    print('=========================')
    input_words = user_input.split()

    # Check if there are three or more words, then delete the last word
    if len(input_words) >= 3:
        input_words.pop()

    formatted_input = ".".join(input_words).lower()
    
    query = f'"{formatted_input}" intext:"student" intext:".ac.id"'
    
    search_results = google_search(query)
    
    for i, result in enumerate(search_results, start=1):
        print(f"Result {i}: {result}")
    print('=========================')
