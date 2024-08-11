#include <iostream>
#include <fstream>
#include <map>

using namespace std;

int main() {
    fstream fin("input.txt");
    long long int n;
    fin >> n;
    map<long long int, long long int> boxes;
    for (long long int i=0; i<n; ++i) {
        string line;
        long long int d, a;
        fin >> d >> a;
        getline(fin, line);
        boxes[d] += a;
    } 
    for (const auto &[key, value] : boxes) {
        cout << key << " " << value << '\n';
    }
    return 0;
}