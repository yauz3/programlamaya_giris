from __future__ import annotations

students: dict[str, float] = {
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

def letter(score: float) -> str:
    if score < 0 or score > 100:
        return "INVALID"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def add_or_update(name: str, score: float) -> bool:
    if not name or score < 0 or score > 100:
        return False
    students[name] = score
    return True

def summary() -> tuple[float, int, str]:
    total = 0.0
    best_name: str | None = None
    best_score = -1.0

    for name, score in students.items():
        total += score
        if score > best_score:
            best_score = score
            best_name = name

    avg = total / len(students) if students else 0.0
    return (avg, len(students), best_name if best_name else "-")

def list_above(threshold: float) -> list[str]:
    names: list[str] = []
    for name, score in students.items():
        if score >= threshold:
            names.append(name)
    return names

def main() -> None:
    while True:
        print("\n1) Harf notu sor  2) Ekle/Güncelle  3) Özet  4) 80+ Liste  5) Çıkış")
        choice = input("Seçim: ").strip()

        if choice == "1":
            name = input("İsim: ").strip()
            if name not in students:
                print("Yok.")
            else:
                sc = float(students[name])
                print(f"{name} -> {sc} -> {letter(sc)}")

        elif choice == "2":
            name = input("İsim: ").strip()
            score_text = input("Puan (0-100): ").strip()
            try:
                sc = float(score_text)
            except ValueError:
                print("Puan sayı olmalı.")
                continue

            ok = add_or_update(name, sc)
            print("Kaydedildi." if ok else "Hatalı giriş.")

        elif choice == "3":
            avg, count, best = summary()
            print(f"Kişi: {count} | Ortalama: {avg:.1f} | En yüksek: {best}")

        elif choice == "4":
            thresh = 80.0
            names = list_above(thresh)
            if names:
                print(f"{thresh}+ olanlar ({len(names)} kişi): {', '.join(names)}")
            else:
                print("Yok")

        elif choice == "5":
            break

        else:
            print("Geçersiz seçim.")

if __name__ == "__main__":
    main()
