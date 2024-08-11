#include <iostream>

using namespace std;

int main(){
    int L, K;
    cin >> L >> K;
    int current, last;
    int middleR = L % 2 == 1 ? L /2 : -1;
    int middle = L / 2 - 1;
    for (int i = 0; i < K; ++i) {
        last = current;
        cin >> current;
        if (current == middleR) {
            cout << middleR;
            break;
        } else if (current > middle) {
            cout << last << " " << current;
            break;
        }
    } 

    return 0;
}