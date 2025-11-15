#include <bits/stdc++.h>
using namespace std;

void solve(int n) {
    vector<int> v(n);
    for (int i = 0; i < n; ++i)
        cin >> v[i];

    vector<int> ve(n + 1, 0);
    for (int i = 0; i < n; ++i)
        ve[i + 1] = v[i] + ve[i];

    vector<int> vd(n + 1, 0);
    int j = 0;
    for (int i = n - 1; i >= 0; --i) {
        vd[j + 1] = v[i] + vd[j];
        j++;
    }

    reverse(vd.begin(), vd.end());

    int ans = INT_MAX;
    for (int i = 0; i <= n; ++i)
        ans = min(ans, abs(ve[i] - vd[i]));

    cout << ans << endl;
}

int main() {
    string line;
    while (getline(cin, line)) {
        if (line.empty()) break;
        stringstream ss(line);
        int n;
        ss >> n;
        solve(n);
    }
    return 0;
}
