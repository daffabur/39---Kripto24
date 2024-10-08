# Nama     : Daffa Burane Nugraha
# NPM      : 140810220039
# Kelas    : A
# Deskripsi: Program Vigenere Cipher
def vigenere_cipher(teks, kunci, mode='encrypt'):
    hasil = []
    panjang_kunci = len(kunci)
    kunci = kunci.upper()
    
    for i, karakter in enumerate(teks):
        if karakter.isalpha():
            # Tentukan nilai geser berdasarkan karakter kunci yang sesuai
            geser = ord(kunci[i % panjang_kunci]) - ord('A')
            
            # Lakukan pergeseran
            if mode == 'encrypt':
                karakter_baru = chr((ord(karakter.upper()) - ord('A') + geser) % 26 + ord('A'))
            else:  # decrypt
                karakter_baru = chr((ord(karakter.upper()) - ord('A') - geser) % 26 + ord('A'))
            
            # Pertahankan huruf besar/kecil asli
            hasil.append(karakter_baru if karakter.isupper() else karakter_baru.lower())
        else:
            hasil.append(karakter)
    
    return ''.join(hasil)

def enkripsi(teks_asli, kunci):
    return vigenere_cipher(teks_asli, kunci, mode='encrypt')

def dekripsi(teks_sandi, kunci):
    return vigenere_cipher(teks_sandi, kunci, mode='decrypt')

def main():
    while True:
        print("\nProgram Vigenère Cipher")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Keluar")
        
        pilihan = input("Masukkan pilihan Anda (1-3): ")
        
        if pilihan == '1':
            teks_asli = input("Masukkan teks yang ingin dienkripsi: ")
            kunci = input("Masukkan kunci enkripsi: ")
            terenkripsi = enkripsi(teks_asli, kunci)
            print(f"Teks terenkripsi: {terenkripsi}")
        
        elif pilihan == '2':
            teks_sandi = input("Masukkan teks yang ingin didekripsi: ")
            kunci = input("Masukkan kunci dekripsi: ")
            terdekripsi = dekripsi(teks_sandi, kunci)
            print(f"Teks terdekripsi: {terdekripsi}")
        
        elif pilihan == '3':
            print("Terima kasih telah menggunakan Program Vigenère Cipher. Sampai jumpa!")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
