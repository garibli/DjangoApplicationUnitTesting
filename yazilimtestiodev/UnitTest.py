## Fuad Garibli Yazılım Testi Ödevi
## birim testleri burada yazılmıştır. 30 tane birim testimiz vardır. 
## 5 birim testi Faker kütüpanesi kullanır
## 10 birim testi parametrized test kullanır
from faker import Faker
import unittest
from JavaAnalyzer import sapmaHesaplayici
from JavaAnalyzer import analyze_java_file
from parameterized import parameterized

class TestSapmaHesaplayici(unittest.TestCase):
    def setUp(self):
        self.fake = Faker()

    def test_sapmaHesaplayici_with_valid_data(self): ## SapmaHesaplayıcıyı doğru parametrelerle test eder
        javadoc_comments = self.fake.random_int(min=0, max=100)
        total_comments = self.fake.random_int(min=0, max=100)
        num_functions = self.fake.random_int(min=1, max=100)
        kod_satir_sayisi = self.fake.random_int(min=1, max=100)
        yg = self.fake.random_int(min=1, max=100)
        yh = self.fake.random_int(min=1, max=100)
        result = sapmaHesaplayici(javadoc_comments, total_comments, num_functions, kod_satir_sayisi,yh,yg)
        self.assertIsInstance(result, str)

    def test_sapmaHesaplayici_with_zero_num_functions(self): ## Sapma hesaplayıcıyı fonksiyon sayı 0 oalrak test eder
        javadoc_comments = self.fake.random_int(min=0, max=100)
        total_comments = self.fake.random_int(min=0, max=100)
        num_functions = 0
        kod_satir_sayisi = self.fake.random_int(min=1, max=100)
        yg = self.fake.random_int(min=1, max=100)
        yh = self.fake.random_int(min=1, max=100)
        result = sapmaHesaplayici(javadoc_comments, total_comments, num_functions, kod_satir_sayisi,yh,yg)
        self.assertEqual(result, "%inf")

    def test_sapmaHesaplayici_with_zero_kod_satir_sayisi(self): ## sapmahesaplayıcıyı kod satır sayısı 0 olarak test eder
        javadoc_comments = self.fake.random_int(min=0, max=100)
        total_comments = self.fake.random_int(min=0, max=100)
        num_functions = self.fake.random_int(min=1, max=100)
        kod_satir_sayisi = 0
        yg = self.fake.random_int(min=1, max=100)
        yh = self.fake.random_int(min=1, max=100)
        result = sapmaHesaplayici(javadoc_comments, total_comments, num_functions, kod_satir_sayisi,yh,yg)
        self.assertEqual(result, "%inf")

    def test_sapmaHesaplayici_with_zero_yh(self): ## yh'yı 0 olarak test eder
        javadoc_comments = self.fake.random_int(min=0, max=100)
        total_comments = self.fake.random_int(min=0, max=100)
        num_functions = self.fake.random_int(min=1, max=100)
        kod_satir_sayisi = self.fake.random_int(min=1, max=100)
        yg = self.fake.random_int(min=1, max=100)
        yh = 0
        result = sapmaHesaplayici(javadoc_comments, total_comments, num_functions, kod_satir_sayisi,yh,yg)
        self.assertEqual(result, "%inf")

    def test_sapmaHesaplayici_with_zero_yg(self): ## yg yi 0 olarak test eder
        javadoc_comments = self.fake.random_int(min=0, max=100)
        total_comments = self.fake.random_int(min=0, max=100)
        num_functions = 0
        kod_satir_sayisi = self.fake.random_int(min=1, max=100)
        yg = 0
        yh = self.fake.random_int(min=1, max=100)
        result = sapmaHesaplayici(javadoc_comments, total_comments, num_functions, kod_satir_sayisi,yh,yg)
        self.assertEqual(result, "%inf")
    
    @parameterized.expand([ ## parametrized test için girilecek verileri ve getirmeleri olduğu çıktıları burada bildiririz
        (0, 0, 0, 0, 0, 0, "%inf"), #1
        (10, 5, 3, 0, 20, 15, "%inf"), #2
        (10, 5, 0, 20, 15, 10, "%inf"), #3
        (10, 5, 3, 20, 0, 10, "%inf"), #4
        (-20, 10, 5, 50, 30, 25, "%inf"), #5
        (20, 20, 5, 50, 25, 30, "20.0%"), #6
        (20, 10, 5, 50, 35, 30, "-14.3%"), #7
        (20, 10, 5, 50, 30, 30, "0.0%"), #8
        (20, 10, 5, 50, 30, 15, "-50.0%"), #9
        (20, 10, 5, 50, -30, 15, "-150.0%"), #10
    ])

    def test_sapmaHesaplayici(self, javadoc_comments, total_comments, num_functions, kod_satir_sayisi, yh, yg, expected_result):
        result = sapmaHesaplayici(javadoc_comments, total_comments, num_functions, kod_satir_sayisi, yh, yg)
        self.assertEqual(result, expected_result) ## sapma hesaplayıcıyı test eder

    def test_all_zero(self):
        result = sapmaHesaplayici(0, 0, 0, 0, 0, 0)
        self.assertEqual(result, "%inf") ## tüm girilenler 0 olarak test eder

    def test_kod_satir_sifir(self): ## kod satır sayısını 0 olarak test eder
        result = sapmaHesaplayici(10, 5, 3, 0, 20, 15)
        self.assertEqual(result, "%inf")

    def test_num_functions_sifir(self): ## fonksiyon sayısını 0 olarak test eder
        result = sapmaHesaplayici(10, 5, 0, 20, 15, 10)
        self.assertEqual(result, "%inf")

    def test_yh_sifir(self): ## yh yi 0 olarak test eder
        result = sapmaHesaplayici(10, 5, 3, 20, 0, 10)
        self.assertEqual(result, "%inf")

    def test_negative_values(self): ## bug ile ve sayre sayesinde, eksi değerili parametre oluşursa test eder
        result = sapmaHesaplayici(-20, 10, 5, 50, 30, 25)
        self.assertEqual(result, "%inf")

    def test_positive_values(self): ## artı değerli parametreler girildiğinde test eder
        result = sapmaHesaplayici(20, 20, 5, 50, 25, 30)
        self.assertEqual(result, "20.0%")

    def test_yg_greater_than_yh(self): ## yg'nin yh den büyük olduğu durumu test eder
        result = sapmaHesaplayici(20, 10, 5, 50, 35, 30)
        self.assertEqual(result, "-14.3%")

    def test_yh_equals_yg(self): ## yg yhye eşit olduğu durumu test eder
        result = sapmaHesaplayici(20, 10, 5, 50, 30, 30)
        self.assertEqual(result, "0.0%")

    def test_yh_one(self): ## yhnin bir olduğu durumu test eder
        result = sapmaHesaplayici(20, 10, 5, 50, 30, 15)
        self.assertEqual(result, "-50.0%")

    def test_yh_negative(self): ## yhnin eksi olduğu durumu test eder
        result = sapmaHesaplayici(20, 10, 5, 50, -30, 15)
        self.assertEqual(result, "-150.0%")
    
    def test_analyze_java_file_class_name(self): ## analyze_java_files de sınıf adının doğru gelip-gelmediğini test eder
        file_content = "class MyClass { }"
        result = analyze_java_file(file_content)
        self.assertEqual(result["Sınıf"], "MyClass")

        ## Aşağıda olan testlerin hepsi farazi uydurulmuş bir kod parçası üzerinde JavaAnalyzerin fonksiyonlarının
        ## doğru çalışıp çalışılmadığını kontrol ederiz

    def test_analyze_java_file_comments(self): ## JavaAnalyzerde yorum satırlarının doğru sayıp sayılmadığını test eder
        file_content = """
        // This is a single-line comment
        /* This is a multi-line
           comment */
        """
        result = analyze_java_file(file_content)
        self.assertEqual(result["Javadoc Satır Sayısı"], 0)
        self.assertEqual(result["Yorum Satır Sayısı"], 1)

    def test_analyze_java_file_loc(self): ## loc doğru hesaplanıp hesaplanmadığını test eder
        file_content = """
                        class MyClass { }"""
        result = analyze_java_file(file_content)
        self.assertEqual(result["LOC"], 1)

    def test_analyze_java_file_code_lines(self): ## sadece kod olan satır sayılarının doğru sayılıp sayılmadığını test eder
        file_content = """
        class MyClass {
            public void method1() {
                // This is a comment
            }
            public void method2() {
                /* This is
                   a multi-line
                   comment */
            }
        }
        """
        result = analyze_java_file(file_content)
        self.assertEqual(result["Kod Satır Sayısı"], 6)

    def test_analyze_java_file_functions(self): ## fonksiyon sayısının doğru sayılıp sayılmadığını test eder
        file_content = """
        class MyClass {
            public void method1() {}
            private int method2(int x, int y) { return x + y; }
        }
        """
        result = analyze_java_file(file_content)
        self.assertEqual(result["Fonksiyon Sayısı"], 2)

if __name__ == '__main__':
    unittest.main()
