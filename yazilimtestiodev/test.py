##Fuad Garibli Yazılım Testi Ödevi
## Bu dosyamız entegrasyon testi için tanımlanmıştır. 5 adet entegrasyon testleri içerir. her testin amacı 
## fonksiyonunun yanında yazılmıştır
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import AnalysisResult

class AnalysisResultTestCase(TestCase):
    def setUp(self): ## kendimizden bir repository linki ve analiz sonucu oluşturuyoruz
        self.repo_url = "https://github.com/garibli/mixedfiles"
        self.file_content = "Sample Java file content"
        self.analysis_result = {
            "Sınıf": "SampleClass",
            "Javadoc Satır Sayısı": 5,
            "Yorum Satır Sayısı": 10,
            "LOC": 50,
            "Kod Satır Sayısı": 40,
            "Fonksiyon Sayısı": 3,
            "Yorum Sapma Yüzdesi": "25.0%"
        }
    
    def test_index_view_with_valid_repo_url(self): ## eğer girilen link geçerliyse positif bir sonuç döndürsün
        response = self.client.post(reverse('index'), {'github_link': self.repo_url})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sonuçlar:")
    
    def test_index_view_with_invalid_repo_url(self): ## eğer girilen link geçersizse invalid döndürsün
        response = self.client.post(reverse('index'), {'github_link': ''})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The link is invalid.")

    def test_index2_view(self): ## index2.html sayfasının döndürülüp-döndürülmediğini denetliyoruz
        response = self.client.get(reverse('index2'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index2.html')

    def test_analysis_result_creation(self): ## Alınan AnalysisResult nesnesinin parametrelerinin, oluşturma sırasında ayarlanan değerlerle eşleştiğini denetler
        AnalysisResult.objects.create(
            file_name='SampleFile.java',
            javadoc_lines=5,
            total_comments=10,
            loc=50,
            kod_satir_sayisi=40,
            num_functions=3,
            yorum_sapma_yuzdesi='25.0%',
            repository_name=self.repo_url
        )
        analysis_result = AnalysisResult.objects.get(file_name='SampleFile.java')
        self.assertEqual(analysis_result.javadoc_lines, 5)
        self.assertEqual(analysis_result.total_comments, 10)
        self.assertEqual(analysis_result.loc, 50)

    def test_analysis_result_datetime(self): ## veritabanında otomatik girilen zamanın doğru girilip girilmediğini denetler
        AnalysisResult.objects.create(
            file_name='SampleFile.java',
            javadoc_lines=5,
            total_comments=10,
            loc=50,
            kod_satir_sayisi=40,
            num_functions=3,
            yorum_sapma_yuzdesi='25.0%',
            repository_name=self.repo_url
        )
        analysis_result = AnalysisResult.objects.get(file_name='SampleFile.java')
        self.assertIsNotNone(analysis_result.analysis_datetime)
        self.assertIsInstance(analysis_result.analysis_datetime, timezone.datetime)
