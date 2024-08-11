#include <iostream>

using namespace std;

int main() {
    int N, i, j;
    cin >> N >> i >> j;
    if (j<i) {
        int temp = i;
        i = j;
        j = temp;
    }
    cout << min(j-i-1, (N+i-1)-j);
    return 0;
}