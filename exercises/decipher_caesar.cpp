#include <bits/stdc++.h>
using namespace std;

int main() {
    string cipher;
    cout << "cipher: ";
    cin >>  cipher;
    for(int i = 0; i < 26; i++) {
        string plain = "";
        for(int j = 0; j < cipher.size(); j++) {
            if(cipher[j] >= 65 && cipher[j] <= 90) {
                plain = plain + char((cipher[j] - 'A' - i + 26) % 26 + 'A');
            }

            if(cipher[j] >= 97 && cipher[j] <= 122) {
                plain = plain + char((cipher[j] - 'a' - i + 26) % 26 + 'a');
            }
        }
        cout << "Key = " << i << " got " << plain << '\n';
    }
}

