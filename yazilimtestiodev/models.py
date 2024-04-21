## Fuad Garibli Yazılım Testi Ödevi
## Bu dosyamızda veritabanında gerekli tabloyu ve onun sütunlarını oluşturmak için gerekli parametreleri giriyoruz.
from django.db import models
from django.utils import timezone

class AnalysisResult(models.Model):
    file_name = models.CharField(max_length=255)
    javadoc_lines = models.IntegerField()
    total_comments = models.IntegerField()
    loc = models.IntegerField()
    kod_satir_sayisi = models.IntegerField()
    num_functions = models.IntegerField()
    yorum_sapma_yuzdesi = models.CharField(max_length=10)
    repository_name=models.CharField(max_length=255)
    analysis_datetime = models.DateTimeField(default=timezone.now)