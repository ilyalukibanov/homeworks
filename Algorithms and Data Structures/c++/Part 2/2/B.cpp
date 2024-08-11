#include <iostream>
#include <vector>

using namespace std;

int main() {
    int maxDist = 0;
    vector<int> stores;
    vector<int> houses;
    for (int i = 0; i < 10; ++i) {
        int type;
        cin >> type;
        if (type == 1) {
            houses.push_back(i);
        } else if (type == 2) {
            stores.push_back(i);
        }
    }
    for (auto house : houses) {
        int minStoreDistance = 10;
        for (auto store : stores) {
            minStoreDistance = min(minStoreDistance, abs(house-store));
        }
        maxDist = max(maxDist, minStoreDistance);
    }
    cout << maxDist;

    return 0;
}