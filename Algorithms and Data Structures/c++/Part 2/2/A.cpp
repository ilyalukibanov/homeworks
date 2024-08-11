#include <iostream>

using namespace std;

int main() {
    unsigned long long int ans, mn = 0;
    while(true) {
        unsigned long long int num;
        cin >> num;
        if (num > mn) {
            ans = 1;
            mn = num;
        } else if (num == mn) {
            ++ans;
        } else if (num == 0) {
            break;
        }
    }
    cout << ans;

    return 0;
}