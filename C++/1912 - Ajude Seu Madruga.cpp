#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    while (true) {
        int n, c;
        cin >> n >> c;

        if (n == 0 && c == 0) break;

        vector<int> v(n);
        for (int i = 0; i < n; ++i) {
            cin >> v[i];
        }

        sort(v.begin(), v.end());

        int esq = 0;
        int dir = v[n - 1];
        double corte = 0.0;

        double aant = 0;
        for (int i = 0; i < n; ++i) {
            aant += v[i];
        }

        if (aant < c) {
            cout << "-.-" << endl;
        } else {
            double dif = aant - c;
            int ii = 1;
            double a = 0.0;

            while (dif >= 0.0001) {
                ++ii;
                a = 0.0;
                corte = (esq + dir) / 2.0;

                for (int i = 0; i < n; ++i) {
                    if (v[i] > corte) {
                        a += v[i] - corte;
                    }
                }

                if (fabs(a - c) < 1e-6) {
                    break;
                } else if (a < c) {
                    dif = fabs(aant - a);
                    aant = a;
                    dir = corte;
                } else {
                    dif = fabs(aant - a);
                    aant = a;
                    esq = corte;
                }
            }

            stringstream ss;
            ss << fixed << setprecision(6) << a;
            string van = ss.str().substr(0, 6);

            if (stof(van) != c) {
                cout << "-.-" << endl;
            } else {
                cout << fixed << setprecision(4) << corte << endl;
            }
        }
    }

    return 0;
}
