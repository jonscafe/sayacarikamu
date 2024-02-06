from googlesearch import search
import os

def google_search(query, num_results=5):
    results = [result for result in search(query, num_results=num_results)]
    return results

def run_linkedin_search(user_input):
    print('LINKEDIN (GOOGLE DORKING)')
    print('=========================')

    query = f'"{user_input}" intext:"linkedin"'

    search_results = google_search(query)

    for i, result in enumerate(search_results, start=1):
        print(f"linkedin account: {result}")
    
    print('=========================')

if __name__ == "__main__":
    run_linkedin_search()
