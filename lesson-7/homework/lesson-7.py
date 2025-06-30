#1.1. is_prime(n) funksiyasi
# is_prime(n) funksiyasini hosil qiling (n > 0). Agar n soni tub bo'lsa True, aks holda False qiymat qaytarsin.

# Misollar:
# Kiritish:
# 4
# Natija:
# False
# (Izoh: 4 soni tub emas, chunki u 2 ga bo'linadi.)


def is_prime(n):
    if n < 2:
        return False  # 0 va 1 tub emas

    for i in range(2, int(n**0.5) + 1):  # faqat √n gacha tekshiriladi
        if n % i == 0:
            return False
    return True
is_prime(5)

#2. digit_sum(k) funksiyasi
#digit_sum(k) funksiyasini yozing, u k sonining raqamlari yig'indisini hisoblaydi.
def digit_sum(k):
    sum=0
    for i in str(k):
       
        sum+=int(i)
    print(sum)
digit_sum(502)

#Ikki sonning darajalari
# Berilgan N sonidan oshmaydigan barcha 2 ning darajalarini (ya'ni, 2**k shaklidagi sonlarni) chop etuvchi funksiyani yozing.

# Misol:
# Kiritish:
# 10
# Natija:
# 2 4 8
# (Izoh: 10 dan kichik yoki teng bo'lgan 2 ning darajalari: 2, 4, 8.)
def powers_of_two(N):
    k = 1
    while k <= N:
        print(k, end=' ')
        k *= 2
powers_of_two(10)
