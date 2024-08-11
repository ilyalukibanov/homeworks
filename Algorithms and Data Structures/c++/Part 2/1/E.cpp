#include <iostream>

using namespace std;

int main() {
    int d, x, y;
    cin >> d >> x >> y;
    int hd = d / 2;
    if ((x >= 0) && (y >= 0) && (x+y <= d)) {
        cout << 0;
    } else if (((x < 0) && (y <= hd)) || ((y < 0) && (x <=hd ))) {
        cout << 1;
    } else if ((y < 0) || ((y >= 0 ) && (x-y >= 0))) {
        cout << 2;
    } else {
        cout << 3;
    }
    return 0;
}