from requests_html import HTMLSession

def pddikti(user_input):
    print('PDDIKTI')
    print('=========================')
    session = HTMLSession()
    search_url = f'https://pddikti.kemdikbud.go.id/search/{user_input}'

    search_response = session.get(search_url)
    search_response.html.render(timeout=10)
    print(search_response)
    mahasiswa_links = search_response.html.find('a[href^="/data_mahasiswa/"]')

    for link in mahasiswa_links[:5]:
        link_url = link.absolute_links.pop()
        link_response = session.get(link_url)
        link_response.html.render(timeout=10)
        link_html_lower = link_response.html.text.lower()
        if user_input.lower() in link_html_lower:
            print(f'{user_input}, PDDIKTI Mahasiswa: {link_url}')
    
    dosen_links = search_response.html.find('a[href^="/data_dosen/"]')
    for link in dosen_links[:5]:
        link_url = link.absolute_links.pop()
        link_response = session.get(link_url)
        link_response.html.render(timeout=10)
        link_html_lower = link_response.html.text.lower()
        if user_input.lower() in link_html_lower:
            print(f'{user_input}, PDDIKTI Dosen: {link_url}')
    
    print('=========================')
    
if __name__ == "__main__":
    pddikti()