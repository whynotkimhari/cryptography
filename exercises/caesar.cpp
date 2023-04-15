#include <bits/stdc++.h>
using namespace std;

int main() {
    int shift;
    string plain;
    cout << "plain text: ";
    cin >> plain;
    cout << endl
        << "key: ";
    cin >> shift;

    string cipher = "";
    for(int i = 0; i < plain.size(); i++) {
        if(plain[i] >= 65 && plain[i] <= 90) {
            cipher = cipher + char((plain[i] - 'A' + shift) % 26 + 'A');
        }

        if(plain[i] >= 97 && plain[i] <= 122) {
            cipher = cipher + char((plain[i] - 'a' + shift) % 26 + 'a');
        }
        
    }
    cout << endl << cipher << endl;
}