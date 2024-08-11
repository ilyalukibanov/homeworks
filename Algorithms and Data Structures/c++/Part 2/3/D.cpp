#include <iostream>
#include <sstream>
#include <string>
#include <unordered_set>
#include <set>
#include <fstream>
#include <algorithm>

using namespace std;

int main() {
    ifstream fin("input.txt");
    int N;
    unordered_set<int> no;
    set<int> options, yes;
    fin >> N;
    string line;
    getline(fin, line);
    while (true) {
        string guesses, answer;
        getline(fin, guesses);
        if (guesses == "HELP") {
            break;
        }
        getline(fin, answer);
        stringstream ss(guesses);
        int x;
        if (answer == "YES") {
            set<int> temp1, temp2;
            while (ss >> x){ 
                temp1.insert(x);
            }
            if (yes.size() == 0) {
                yes = temp1;
            } else {
                set_intersection(yes.begin(), yes.end(), temp1.begin(), temp1.end(), inserter(temp2, temp2.begin()));
                yes = temp2;
            }
        } else {
            while (ss >> x){ 
                no.insert(x);
            }
        }
    }
    if (yes.size() > 0) {
        for (int y : yes) {
            options.insert(y);
        }
    } else {
        for (int i=1;i<=N;++i) {
        options.insert(i);
    }
    }
    for (int n : no) {
        options.erase(n);
    }
    for (int x : options) {
        cout << x << " ";
    }

    return 0;
}