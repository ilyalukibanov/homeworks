#include <iostream>
#include <string>

using namespace std;

int main() {
    string s;
    cin >> s;
    int n = size(s);
    int cost = 0;
    cout << n/2;
    for (int i = 0; i < (n/2); ++i) {
        cout << i << s[n-i-1];
        if (s[i] != s[n-i-1]) {
            ++cost;
        }
    }
    cout << cost;

    return 0;
}