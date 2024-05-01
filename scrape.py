import requests
import json
from bs4 import BeautifulSoup

url = 'https://www.google.com/about/careers/applications/jobs/results/?q=python'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = soup.find_all('li', class_='lLd3Je')
    jobs_data = []  # a list to store jobs data
    
    for job in jobs:
        title = job.find('h3', class_='QJPWVe').text.strip()
        company_name = job.find('span', class_='RP7SMd').text.strip()
        
        location_element = job.find('span', class_='r0wTof')
        location = location_element.text.strip() if location_element else ''
        
        skill_level_element = job.find('span', class_='wVSTAb')
        skill_level = skill_level_element.text.strip() if skill_level_element else ''
        
        job_url_element = job.find('a', class_='WpHeLc')
        job_url = job_url_element['href'] if job_url_element else ''
        
        
        job_data = {
            'title': title,
            'company': company_name,
            'location': location,
            'skill_level': skill_level,
            'job_url': job_url
        }
        jobs_data.append(job_data)
        
    with open('jobs.json', 'w') as f:
        json.dump(jobs_data, f, ensure_ascii=False, indent=4)   
        
    print('Successfully saved the data to jobs.json')
else:
    print('Failed to fetch the page. Status code:', response.status_code)



# if response.status_code == 200:
#     with open('page.html', 'w', encoding='utf-8') as f:
#         f.write(response.text)
#     print('Successfully saved the file')
# else:
#     print('Failed to fetch the page. Status code:', response.status_code)