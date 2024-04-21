## Fuad Garibli Yazılım Testi Ödevi
## Uygulamamızın kalbi olan bu dosyada, github depolarından getirilen .java dosyalarının analizi yapılmakta 
## ve gerekli parametreleri döndürülmektedir.
import re
def sapmaHesaplayici(num_lines, total_comments, num_functions, kod_satir_sayisi,yh,yg):
  if num_lines<0 or  total_comments<0 or num_functions<0:
     return "%inf"
  if kod_satir_sayisi ==0:
     return "%inf"
  if num_functions == 0:
        return "%inf"
  if yh == 0:
        return "%inf"
  else:
       yorum_sapma_yuzdesi = ((100 * yg) / yh) - 100
       return f"{round(yorum_sapma_yuzdesi, 2):.1f}%"
##Before
def analyze_java_file(file_content):
    class_name = re.search(r'class\s+(\w+)', file_content)
    class_name = class_name.group(1) if class_name else None #sınıf adını döndür
    #yorum satırı sayısı hesaplayıcı
    comments = re.findall(r'(?ms://\s*([^\n]*)|/\*([^*]|(\*+[^*/]))*\*/)', file_content)
    total_comments = 0
    in_block_comment = False
    for comment in comments:
        if isinstance(comment, tuple):
            comment = comment[0]
        lines = comment.split('\n')
        for line in lines:
            line = line.strip()
            if line and not (line.startswith('*') or '@' in line or '<p>' in line):
                total_comments += 1
            if '/*' in line:
                in_block_comment = True
            if '*/' in line:
                in_block_comment = False
                total_comments += 1
            if in_block_comment and not (line.startswith('*') or '@' in line or '<p>' in line):
                total_comments += 1
    #Kod satır sayısı hesaplayıcı
    code_lines = file_content.split('\n')
    loc = len(code_lines)-1
    kod_satir_sayisi = 0
    in_comment_block = False
    for line in code_lines:
        stripped_line = line.strip()
        if stripped_line and not stripped_line.startswith('//'):
            if stripped_line.startswith('/*'):
                in_comment_block = True
                continue
            if in_comment_block:
                if stripped_line.endswith('*/'):
                    in_comment_block = False
                continue
            kod_satir_sayisi += 1
    #fonksiyon sayısı hesaplayıcı
    num_functions = len(re.findall(r'(\w+)\s+(\w+)\s*\([^)]*\)\s*{', file_content))
    #javadoc hesaplayıcı
    javadoc_comments = sum(1 for comment in re.findall(r'/\*\*(.*?)\*/', file_content, re.DOTALL) 
                       if comment.strip()  # Check for non-empty comment
                       for line in comment.strip().splitlines()  # Split non-empty comment
                       if not (line.isspace() or '<p>' in line))
   

    ##yg yh hesaplayıcı
    if num_functions == 0:
        yg = "undefined"
        yh = "undefined"
    else:
        yg = ((javadoc_comments + total_comments) * 0.8) / num_functions
        yh = (kod_satir_sayisi / num_functions) * 0.3
    ##değer döndürücü
    return {
        "Sınıf": class_name,
        "Javadoc Satır Sayısı": javadoc_comments,
        "Yorum Satır Sayısı": total_comments,
        "LOC": loc,
        "Kod Satır Sayısı": kod_satir_sayisi,
        "Fonksiyon Sayısı": num_functions,
        "Yorum Sapma Yüzdesi": sapmaHesaplayici(javadoc_comments, total_comments, num_functions, kod_satir_sayisi, yh, yg)
    }