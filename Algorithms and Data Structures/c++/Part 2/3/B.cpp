#include <iostream>
#include <sstream>
#include <unordered_set>
#include <string>

using namespace std;

int main() {
    unordered_set<int> numbers;
    int x;
    string line;
    getline(cin, line);
    stringstream ss(line);
    while (ss >> x) {
        if (numbers.count(x)) {
            cout << "YES\n";
        } else {
            numbers.insert(x);
            cout << "NO\n";
        }
    }

    return 0;
}