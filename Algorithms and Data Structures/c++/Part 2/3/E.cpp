#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

int main(){
    int M, N;
    string line;
    ifstream fin("input.txt");
    fin >> M;
    string witnesses [M];
    getline(fin, line);
    for (int i=0; i<M; ++i) {
        getline(fin, line);
        witnesses[i] = line;
    }
    fin >> N;
    string plates [N];
    getline(fin, line);
    for (int i=0; i<N; ++i) {
        getline(fin, line);
        plates[i] = line;
    }

    int maxCounter = 0;
    vector<string> suspects;
    for (string plate : plates) {
        unordered_set<char> plateSymbols;
        for (char symbol : plate) {
            plateSymbols.insert(symbol);
        }
        int counter = 0;
        for (string witness : witnesses) {
            bool is_subset = true;
            for (char symbol : witness) {
                if (!plateSymbols.count(symbol)) {
                    is_subset = false;
                    break;
                }
            }
            if (is_subset) {
                ++counter;
            }
        }
        if (counter > maxCounter) {
            vector<string> sus;
            sus.push_back(plate);
            suspects = sus;
            maxCounter = counter;
        } else if (counter == maxCounter) {
            suspects.push_back(plate);
        }
    }
    for (string suspect : suspects) {
        cout << suspect << '\n';
    }

    return 0;
}