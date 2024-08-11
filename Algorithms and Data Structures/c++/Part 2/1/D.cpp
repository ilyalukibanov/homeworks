#include <iostream>

using namespace std;

int main() {
    int N;
    cin >> N;
    for (int i = 0; i < N; ++i) {
        int coord;
        cin >> coord;
        if (i == N / 2) {
            cout << coord;
            break;
        }
    }

    return 0;
}