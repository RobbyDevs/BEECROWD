#include <bits/stdc++.h>

using namespace std;

const int MOD = 1e9 + 7;

int main() {
    string line;

    while (getline(cin, line)) {
        int n, k;

        stringstream ss(line);
        if (!(ss >> n >> k)) {
            // linha com apenas n
            n = stoi(line);
            string kline;
            getline(cin, kline);
            k = stoi(kline);
        }

        vector<int> va;
        int le = 0;
        while (le < n) {
            string data;
            getline(cin, data);
            stringstream ds(data);
            int num;
            while (ds >> num) {
                va.push_back(num);
                le++;
            }
        }

        sort(va.begin(), va.end());

        long long c = 0;
        for (int i = va.size() - 1; i >= n - k; --i) {
            c = (c + (va[i] % MOD)) % MOD;
        }

        cout << c << endl;
    }

    return 0;
}
