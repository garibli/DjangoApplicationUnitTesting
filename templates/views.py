## Fuad Garibli Yazılım Testi Ödevi
## bu dosyada çağırılan her .html dosyasının neyi göstereceğini ayarladık. index.html viewinde her defasında submit
## butonuna tıklandığında veritabanına analiz sonuçlarını aktarması için ayarlamalar yaptık

from django.shortcuts import render
from django.http import HttpResponse
from yazilimtestiodev.main import fetch_java_files, analyze_java_file
import requests
from yazilimtestiodev.models import AnalysisResult
from django.utils import timezone

def index(request):
    if request.method == 'POST':
        repo_url = request.POST.get('github_link')
        if repo_url:
            java_files = fetch_java_files(repo_url)
            if java_files:
                analysis_results = []
                for java_file_url in java_files:
                    response = requests.get(java_file_url)
                    if response.status_code == 200:
                        file_content = response.text
                        analysis_result = analyze_java_file(file_content)
                        analysis_obj = AnalysisResult(
                            file_name=java_file_url.split('/')[-1],
                            javadoc_lines=analysis_result['Javadoc Satır Sayısı'],
                            total_comments=analysis_result['Yorum Satır Sayısı'],
                            loc=analysis_result['LOC'],
                            kod_satir_sayisi=analysis_result['Kod Satır Sayısı'],
                            num_functions=analysis_result['Fonksiyon Sayısı'],
                            yorum_sapma_yuzdesi=analysis_result['Yorum Sapma Yüzdesi'],
                            repository_name=repo_url
                        )
                        analysis_obj.save()
                        analysis_results.append({
                            'file_name': analysis_obj.file_name,
                            'repository_name': analysis_obj.repository_name,
                            'analysis_datetime': analysis_obj.analysis_datetime,
                            'analysis': analysis_result
                        })
                return render(request, 'index.html', {'analysis_results': analysis_results})
            else:
                return HttpResponse("No Java files found in the provided GitHub repository.")
        else:
            return HttpResponse("The link is invalid.")
    else:
        return render(request, 'index.html')

def index2(request):
    analysis_results = AnalysisResult.objects.all()
    return render(request, 'index2.html', {'analysis_results': analysis_results})