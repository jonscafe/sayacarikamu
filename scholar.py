from requests_html import HTMLSession

def scholar(user_input):
    print('SCHOLAR')
    print('=========================')
    session = HTMLSession()
    search_url = f'https://scholar.google.com/citations?view_op=search_authors&mauthors={user_input}&hl=id&oi=ao'

    search_response = session.get(search_url)
    print(search_response)
    search_response.html.render(timeout=10)
    user_input_lower = user_input.lower()
    info_author = search_response.html.text.lower()

    if user_input_lower in info_author:
        index = info_author.find(user_input_lower)
        
        name_and_affiliation_line = info_author[index:].split('\n')[0].strip()

        if ' Afliasi: ' in name_and_affiliation_line:
            name_index = name_and_affiliation_line.find(' Afliasi: ')
            name = name_and_affiliation_line[:name_index].strip()
            print('Nama:', name)
        else:
            print('Nama:', name_and_affiliation_line)

        print('Link Scholar:', search_response.url)
    else:
        print(f'No information found for {user_input}')
    
    print('=========================')
    
if __name__ == "__main__":
    scholar()