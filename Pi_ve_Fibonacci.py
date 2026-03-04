import math

def get_choice() -> int:
    """Kullanıcıdan 1 (pi) veya 2 (fibonacci) seçimini alır."""
    while True:
        choice_str = input("Pi için 1, Fibonacci için 2 seçin: ").strip()
        if choice_str in ("1", "2"):
            return int(choice_str)
        print("Hata: Lütfen 1 veya 2'yi seçin.")

def get_n() -> int:
    """Kullanıcıdan N değerini alır (tamsayı)."""
    while True:
        n_str = input("N değerini girin (0-7): ").strip()
        try:
            n = int(n_str)
            return n
        except ValueError:
            print("Hata: N bir tamsayı olmalı.")

def validate_n(n: int) -> bool:
    """
    N > 7 ise çalıştırmaz.
    True: devam edilebilir, False: durdur.
    """
    if n > 7:
        print(f"Lütfen {n} sayısını azaltınız.")
        return False
    return True

def print_pi_to_n_decimals(n: int) -> None:
    """Pi sayısını N basamak (ondalık) hassasiyetle yazdırır."""
    # N = 0 ise sadece tam kısmı yazar (3)
    pi_str = f"{math.pi:.{n}f}"
    print(f"π (N={n} basamak): {pi_str}")

def sum_fibonacci_up_to_n(n: int) -> int:
    """
    N dahil olmak üzere (<=N) tüm Fibonacci sayılarını toplar.
    Örn: N=7 için fib: 0,1,1,2,3,5 -> toplam 12
    """
    a, b = 0, 1
    total = 0
    while a <= n:
        total += a
        a, b = b, a + b
    return total

def main() -> None:
    choice = get_choice()
    n = get_n()

    if not validate_n(n):
        return  # program burada biter

    if choice == 1:
        print_pi_to_n_decimals(n)
    else:  # choice == 2
        total = sum_fibonacci_up_to_n(n)
        print(f"N={n} için (<=N) Fibonacci toplamı: {total}")

if __name__ == "__main__":
    main()
