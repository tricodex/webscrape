import requests

def get_html(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        with open('page.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
        print('Successfully saved the file')
    else:
        print('Failed to fetch the page. Status code:', response.status_code)

    
if __name__ == '__main__':
    
    url = 'https://www.google.com/about/careers/applications/jobs/results/?q=python'
    get_html(url)