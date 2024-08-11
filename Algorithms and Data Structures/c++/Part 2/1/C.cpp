#include <iostream>

using namespace std;

int main () {
    int x, y, z;
    cin >> x >> y >> z;
    if ((y > 12) or (x > 12)) {
        cout << 1;
    } else if ((x == y) and (x <= 12)) {
        cout << 1;
    } else {
        cout << 0;
    }
    return 0;
}