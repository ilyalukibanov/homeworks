#include <iostream>
#include <sstream>
#include <string>
#include <set>

using namespace std;

int main(){
    int x, commonElements=0;
    set<int> A;
    string line;
    getline(cin, line);
    stringstream ss1;
    ss1 << line;
    while (ss1 >> x) {
        A.insert(x);
    }
    getline(cin, line);
    stringstream ss2;
    ss2 << line;
    while (ss2 >> x) {
        if (A.count(x)) {
            ++commonElements;
        }
    }
    cout << commonElements;
    return 0;
}