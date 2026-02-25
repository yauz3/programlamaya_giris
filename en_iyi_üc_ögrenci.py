# For loop ile: not analizi + harf notu + top-3 + özet istatistik

students = [
    {"name": "Ayşe",  "scores": [78, 91, 84]},
    {"name": "Mehmet","scores": [65, 72, 70]},
    {"name": "Zeynep","scores": [92, 88, 95]},
    {"name": "Can",   "scores": [55, 60, 58]},
    {"name": "Elif",  "scores": [80, 77, 83]},
]

def letter_grade(avg: float) -> str:
    if avg >= 90: return "A"
    if avg >= 80: return "B"
    if avg >= 70: return "C"
    if avg >= 60: return "D"
    return "F"

results = []  # her öğrenci için (isim, ortalama, harf) tutulacak
total_sum = 0.0
total_count = 0
best_avg = -1.0
best_name = None

# Ana for loop: her öğrenciyi dolaş
for s in students:
    name = s["name"]
    scores = s["scores"]

    # İç içe for loop: notları dolaşarak ortalama hesapla
    s_sum = 0
    for sc in scores:
        s_sum += sc
    avg = s_sum / len(scores)

    grade = letter_grade(avg)
    results.append((name, avg, grade))

    # genel istatistikler için birikimli toplama
    total_sum += s_sum
    total_count += len(scores)

    # en iyi öğrenciyi bul
    if avg > best_avg:
        best_avg = avg
        best_name = name

class_avg = total_sum / total_count

# Top-3 öğrenciyi bulmak için results’u ortalamaya göre sırala (bunu da for ile göstereceğiz)
sorted_results = sorted(results, key=lambda x: x[1], reverse=True)
top_n = 3
top3 = []
for i in range(min(top_n, len(sorted_results))):
    top3.append(sorted_results[i])

# Şartlı filtreleme: ortalaması 80+ olanlar
above_80 = []
for name, avg, grade in results:
    if avg >= 80:
        above_80.append(name)

# Rapor
print("=== Öğrenci Raporu ===")
for name, avg, grade in results:
    print(f"{name:7s} | Ortalama: {avg:5.1f} | Harf: {grade}")

print("\n=== Sınıf Özeti ===")
print(f"Sınıf ortalaması: {class_avg:.1f}")
print(f"En iyi öğrenci: {best_name} ({best_avg:.1f})")

print("\n=== Top-3 ===")
for rank, (name, avg, grade) in enumerate(top3, start=1):
    print(f"{rank}. {name} - {avg:.1f} ({grade})")

print("\n=== 80+ Ortalama Olanlar ===")
print(", ".join(above_80) if above_80 else "Yok")
