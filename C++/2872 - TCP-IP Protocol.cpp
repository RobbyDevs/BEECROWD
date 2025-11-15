#include <bits/stdc++.h>

using namespace std;

int main() {
    int caso = 0;
    string n;

    while (true) {
        caso++;

        if (!(cin >> n)) {
            break; 
        }

        //if (caso > 1){
        //    cout<<endl;
        //}
        vector<string> v;

        if (n == "1") {
            while (true) {
                string a, b;
                if (!(cin >> a)) break;
                if (a == "0") break;

                cin >> b;
                v.push_back(b);
            }

            sort(v.begin(), v.end());

            for (const string& i : v) {
                cout << "Package " << i << endl;
            }
            cout<<endl;
        }
    }

    return 0;
}
