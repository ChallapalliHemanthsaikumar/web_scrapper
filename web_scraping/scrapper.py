import requests
from bs4 import BeautifulSoup
import re 
import time
import os
from uuid import uuid4
def collector_of_links(url,output_file):
    "This function which collects links from the given links and stores it in specifed file "
    print(url[0])
    links ,response= extract_links(url[0])

    if response.status_code == 200:
        extract_text(response)

    try:
        with open(output_file, 'w') as file:
            for link in links:
                file.write(link + '\n')
        print(f"Links collected and stored in '{output_file}' successfully.")
        return "success"
    except Exception as e:
        print(f"An error occurred: {e}")


def process_links(links):
    processed_links = []
    keyword = "amnesia"

    for link in links:
        if re.search(keyword, link, re.IGNORECASE):
            if link.startswith("https"):
                processed_links.append(link)
            elif link.startswith("/search"):
                processed_links.append("https://www.google.com" + link)
            elif "https://" in link:
                # Extract the part of the link containing "https://" and append it
                match = re.search(r"https://\S+", link)
                if match:
                    processed_links.append(match.group(0))
            else:
                # Skip other types of links
                pass

    return processed_links





def extract_links(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all <a> tags (links) in the HTML content
            links = soup.find_all('a', href=True)
            
            # Extract the href attribute (link) from each <a> tag
            extracted_links = [link['href'] for link in links]

            links = process_links(extracted_links)
                
            
            # Return the extracted links
            return links,response
            
        else:
            print(f'Failed to retrieve data from the URL: {url}. Status code: {response.status_code}')
            return None
    
    except requests.exceptions.RequestException as e:
        print(f'Error occurred while fetching data from the URL: {url}. Error: {e}')
        return None

# Example usage:

def extract_text(response):
    soup = BeautifulSoup(response.content, 'html.parser')

    text = soup.get_text()


    
            # Apply regex to extract text containing occurrences of "amnesia"
    matches = re.findall(r'\b(amnesia)\b', text, re.IGNORECASE)

    if len(matches) != 0:
        
        topic = "amnesia" + str(uuid4())

        

        try:
            if len(text) >= 0:
                with open('./web_scraping/raw/'+ topic + '.txt', 'w') as file:
                
                    file.write(text + '\n')
            
        except Exception as e:
            print(f"An error occurred: {e}")

            
            # Return the matches
   

def verify(link):

    try:
        response = requests.get(link)
        if response.status_code != 200:
            result = False
        else:
            result = True
        return response,result
    except Exception as error:

        result = False
        return "fail",result


def recursive(response):
    soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all <a> tags (links) in the HTML content
    links = soup.find_all('a', href=True)
            
            # Extract the href attribute (link) from each <a> tag
    extracted_links = [link['href'] for link in links]

    links = process_links(extracted_links)

    

    try:
        topic = "amnesia" + str(uuid4())    
        with open('./web_scraping/raw_links/'+ topic + '.txt', 'w') as file:
            for link in links:
                file.write(link + '\n')

            
            
    except Exception as e:
        print(f"An error occurred: {e}")




def collect_data(links,text_file):
    


    with open(links,'r') as r:
        links_list = r.readlines()

    for link in links_list:

        response,result = verify(link)
        if result:
            extract_text(response)
            recursive(response)
    if os.path.exists(links):        
        os.remove(links)
    

    return "success"    

def collected_data(file_path,links_list):
    for link in links_list:

        response,result = verify(link)
        if result:
            extract_text(response)
            recursive(response)
    if os.path.exists(file_path):        
        os.remove(file_path)


