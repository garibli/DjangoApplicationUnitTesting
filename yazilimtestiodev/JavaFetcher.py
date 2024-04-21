## FUad Garibli Yazılım Testi Ödevi
## Bu dosyamızda github repositorysına bağlanıyoruz. Oradayı .java dosyalarını getiriyoruz. Analiz ve sayre
## JavaAnalyzer.py dosyasında yapılmaktadır. 
import requests
import re

def fetch_java_files(repo_url):
    api_url = repo_url.replace("github.com", "api.github.com/repos") + "/contents"
    response = requests.get(api_url)
    contents = response.json()
    java_files = []

    for item in contents:
        if item["name"].endswith(".java"):
            file_url = item["download_url"]
            response = requests.get(file_url)
            file_content = response.text
            if re.search(r'class\s+(\w+)', file_content):
                java_files.append(file_url)

    return java_files
