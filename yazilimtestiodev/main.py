## Fuad Garibli Yazılım Testi Ödevi
## Bu dosyamız uygulamamızı djangodan bağımsız olarak, direk terminal üzerinden kendimizin çalıştırıp
## ".java" dosyalarını getirtmek ve analizlerini yapmak için kullanıyoruz. Basit bir main dosyasıdır
import requests
import re
from JavaFetcher import fetch_java_files
from JavaAnalyzer import analyze_java_file

if __name__ == "__main__":
    repo_url = input("Github Linkini Giriniz: ")
    java_files = fetch_java_files(repo_url)

    for java_file_url in java_files:
        response = requests.get(java_file_url)
        file_content = response.text

        analysis_result = analyze_java_file(file_content)

        print("\nAnaliz ediliyor: ", java_file_url.split('/')[-1])
        for key, value in analysis_result.items():
            print(key + ":", value)