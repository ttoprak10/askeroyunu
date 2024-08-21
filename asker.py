import random
import time

basker = 100

def baslangic():
    global basker
    askernasil = input("Asker türünüzü seçiniz (1 Türk, 2 Yabancı): ")
    
    if askernasil == '1':
        print("Hoşgeldin Türk Askeri.")
        print("Ben Albay Toprak")
        print("Sana Oyunu Öğreteceğim")
        atla = input("Eğitimi geçmek istermisin? (evet/hayır): ")
        if atla.lower() == "evet":
            menu()
        else:
            print("Eğitim başlıyor...")
            egitim_yap()
            menu()
    elif askernasil == '2':
        print("Hoşgeldin Yabancı Asker.")
        print("Eğitim başlangıcı...")
        egitim_yap()
        menu()
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
        baslangic()

def egitim_yap():
    global basker
    print("Eğitim yapılıyor...")
    time.sleep(3)
    for _ in range(3):
        print("Eğitim devam ediyor...")
        time.sleep(3)
    basker += random.randint(1, 10)  # Eğitim sonrası askerin sağlığı artar
    print(f"Eğitim tamamlandı. Güncel asker sağlığı: {basker}")

def savas():
    global basker
    print("Savaşa gidiyorsun...")
    time.sleep(3)
    dusman_saglik = random.randint(50, 100)  # Düşmanın sağlık durumu
    print(f"Düşmanın sağlığı: {dusman_saglik}")

    while dusman_saglik > 0 and basker > 0:
        # Savaşta oyuncunun hamlesi
        hamle = input("Saldırmak için 'saldır' yazın veya savaşı bırakmak için 'geri' yazın: ")
        if hamle.lower() == 'saldır':
            hasar = random.randint(10, 30)  # Oyuncunun verdiği hasar
            dusman_saglik -= hasar
            print(f"Düşmana {hasar} hasar verdiniz. Düşmanın kalan sağlığı: {dusman_saglik}")

            if dusman_saglik <= 0:
                print("Düşmanı yendiniz!")
                basker += 20  # Düşmanı yendikten sonra askerin sağlığı artar
                print(f"Savaş tamamlandı. Güncel asker sağlığı: {basker}")
                return
            else:
                # Düşmanın karşı saldırısı
                dusman_hamlesi = random.randint(5, 20)
                basker -= dusman_hamlesi
                print(f"Düşman size {dusman_hamlesi} hasar verdi. Güncel asker sağlığı: {basker}")
                if basker <= 0:
                    print("Asker öldü. Oyun sona erdi.")
                    return
        elif hamle.lower() == 'geri':
            print("Savaştan geri çekiliyorsunuz.")
            return
        else:
            print("Geçersiz komut. Lütfen tekrar deneyin.")

def menu():
    global basker
    while True:
        print(f"Asker Sayın {basker}")
        print("Ne yapmak istiyorsun?")
        print("1. Savaş")
        print("2. Asker Eğit")
        print("3. Eğitim Yap")
        print("4. Çıkış")
        
        neyapcan = input("Seçiminizi yapın (1-4): ")
        
        if neyapcan == '1':
            savas()
        elif neyapcan == '2':
            print("Askeri eğitiyorsun...")
            basker += random.randint(1, 10) # Askeri eğitmenin sonucu olarak askerin sağlığı artar
            print(f"Eğitim sonrası asker sağlığı: {basker}")
        elif neyapcan == '3':
            egitim_yap()
        elif neyapcan == '4':
            print("Oyundan çıkıyorsunuz...")
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    baslangic()
