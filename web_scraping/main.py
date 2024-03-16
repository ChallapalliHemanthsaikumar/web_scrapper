
from scrapper import collector_of_links,collect_data,collected_data

import os
import time


with open('./web_scraping/website_url.txt','r') as r:
    link = r.readlines()

def time_checker():
    directory_path = "./web_scraping/raw_links"
    if os.path.exists(directory_path):
        files = os.listdir(directory_path)
        current_time = time.time()
        for file in files:
            file_path = os.path.join(directory_path, file)
            if os.path.isfile(file_path):
                file_creation_time = os.path.getmtime(file_path)
                if current_time - file_creation_time < 600:  # 600 seconds = 10 minutes
                    os.remove(file_path)
                    print(f"File {file} created within the last 10 minutes has been removed.")
    else:
        print("Directory does not exist.")



def file_size_checker():
    directory_path = "./web_scraping/raw"

    if os.path.exists(directory_path):
        files = os.listdir(directory_path)
        for file in files:
            file_path = os.path.join(directory_path, file)
            if os.path.isfile(file_path) and os.path.getsize(file_path) == 0:
                os.remove(file_path)
                print(f"Empty file {file} has been removed.")
    else:
        print("Directory does not exist.")
    
def recursor():
    file_size_checker()
    time_checker()
    file_path = './web_scraping/raw_links'
    if os.path.exists(file_path):
        files = os.listdir(file_path)

    for file in files:
        print(file)
        if os.path.exists(file_path+ '/' + file):

            with open(file_path+ '/' + file,'r') as r:
                links =  r.readlines()
            collected_data(file_path + '/'+file,links)
        
    recursor()    



success = collector_of_links(link,'./web_scraping/urls.txt')
if success == "success":

    result = collect_data('./web_scraping/urls.txt','./web_scraping/raw/amensia.txt')
    print("success")
if result == "success":

    recursor()
    
