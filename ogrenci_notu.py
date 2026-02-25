# 10 öğrencilik sözlük + fonksiyon: isim gir -> harf notu döndür

students = {
    "Ayse": 78,
    "Mehmet": 65,
    "Zeynep": 92,
    "Can": 55,
    "Elif": 80,
    "Ali": 73,
    "Deniz": 88,
    "Ece": 60,
    "Kerem": 49,
    "Seda": 95,
}

def get_letter_grade(student_name: str) -> str:
    """
    Öğrenci adını alır, harf notunu döndürür.
    Eğer isim yoksa veya puan geçersizse uygun mesaj döndürür.
    """
    if student_name not in students:
        return "Öğrenci bulunamadı."

    score = students[student_name]

    if score < 0 or score > 100:
        return "Geçersiz puan."

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Örnek kullanım:
name = input("Öğrenci ismi gir: ").strip()
print(get_letter_grade(name))
