#include <iostream>
#include <sstream>
#include <fstream>
#include <map>
#include <string>

using namespace std;

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    ifstream fin("input.txt");
    map<string, long long int> results;
    while (fin) {
        string line;
        getline(fin, line);
        stringstream ss(line);
        string name;
        long long int votes;
        ss >> name >> votes;
        map<string, long long int>::iterator itr = results.find(name);
        if (itr == results.end()) {
            results.insert({name, votes});
        } else {
            itr->second += votes;
        }
    }
    map<string, long long int>::iterator itr;
    for( itr = results.begin(); itr != results.end(); ++itr) {
        cout << itr->first << " " << itr->second << '\n';
    }

    return 0;
}