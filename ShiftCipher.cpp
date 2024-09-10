#include <iostream>
#include <string>

using namespace std;

string encryptMessage(string message, int key) {
    string encryptedText = "";

    // Iterasi untuk setiap karakter pada string
    for (int i = 0; i < message.length(); i++) {
        char currentChar = message[i];

        // Cek apakah karakter adalah huruf
        if (isalpha(currentChar)) {
            char startingChar = isupper(currentChar) ? 'A' : 'a';
            // Geser karakter dan tambahkan ke string hasil
            encryptedText += char(int(startingChar + (currentChar - startingChar + key) % 26));
        } else {
            // Tambahkan karakter asli jika bukan huruf
            encryptedText += currentChar;
        }
    }
    return encryptedText;
}

string decryptMessage(string message, int key) {
    // Proses dekripsi sama dengan enkripsi, hanya saja kunci dibalik
    return encryptMessage(message, 26 - key);
}

int main() {
    string inputText;
    int shiftKey;

    cout << "Masukkan Pesan: ";
    getline(cin, inputText);
    cout << "Masukkan Kunci Perpindahan: ";
    cin >> shiftKey;

    string encryptedText = encryptMessage(inputText, shiftKey);
    string decryptedText = decryptMessage(encryptedText, shiftKey);

    cout << "Pesan Setelah Enkripsi: " << encryptedText << endl;
    cout << "Pesan Setelah Dekripsi: " << decryptedText << endl;

    return 0;
}