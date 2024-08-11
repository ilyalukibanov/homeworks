#include <iostream>

using namespace std;

int main(){
    int sum = 0;
    int max = 0;
    int N;
    cin >> N;
    for (int i = 0; i < N; ++i) {
        int file;
        cin >> file;
        max = file > max ? file : max;
        sum += file;
    }
    cout << (sum-max);

    return 0;
}