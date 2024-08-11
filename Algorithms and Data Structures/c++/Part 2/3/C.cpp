#include <iostream>
#include <sstream>
#include <unordered_set>
#include <string>
#include <list>
#include <algorithm>

using namespace std;

int main() {
    list<int> unique;
    unordered_set<int> twoPlus;
    int x;
    string line;
    getline(cin, line);
    stringstream ss(line);
    while (ss >> x) {
        if (twoPlus.count(x)) {}
        else if (std::find(unique.begin(), unique.end(), x) != unique.end()) {
            twoPlus.insert(x);
            unique.remove(x);
        } else {
            unique.push_back(x);
        }
    }
    for (int num : unique) {
        cout << num << " ";
    }


    return 0;
}