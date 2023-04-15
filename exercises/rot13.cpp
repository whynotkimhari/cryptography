#include <bits/stdc++.h>
using namespace std;

string encrypt_rot13(string plain);
string decrypt_rot13(string cipher);

int main() {
    string to_encrypt, to_decrypt;
    cout << "text to encrypt: ";
    cin >> to_encrypt;
    cout << "text to decrypt: ";
    cin >> to_decrypt;
    cout << "encrypted text: " << encrypt_rot13(to_encrypt) << '\n'
        << "decrypted text: " << decrypt_rot13(to_decrypt) << '\n';
}

string encrypt_rot13(string plain) {
    string cipher = "";
    for(int i = 0; i < plain.size(); i++) {
        if(plain[i] >= 65 && plain[i] <= 90) {
            cipher = cipher + char((plain[i] - 'A' + 13) % 26 + 'A');
        }

        if(plain[i] >= 97 && plain[i] <= 122) {
            cipher = cipher + char((plain[i] - 'a' + 13) % 26 + 'a');
        }
    }
    return cipher;
}

string decrypt_rot13(string cipher) {
    string plain = "";
    for(int j = 0; j < cipher.size(); j++) {
        if(cipher[j] >= 65 && cipher[j] <= 90) {
            plain = plain + char((cipher[j] - 'A' - 13 + 26) % 26 + 'A');
        }

        if(cipher[j] >= 97 && cipher[j] <= 122) {
            plain = plain + char((cipher[j] - 'a' - 13 + 26) % 26 + 'a');
        }
    }
    return plain;
}