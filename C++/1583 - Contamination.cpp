#include <bits/stdc++.h>

using namespace std;

int main() {
    while (true) {
        int l, c;
        cin >> l >> c;
        if (l == 0 && c == 0)
            break;

        bool isclean = false;
        vector<vector<char>> m(l, vector<char>(c));

        
        for (int i = 0; i < l; i++) {
            string t;
            cin >> t;
            for (int j = 0; j < c; j++) {
                m[i][j] = t[j];
            }
        }

        
        while (!isclean) {
            isclean = true;
            vector<vector<char>> temp = m; 
            for (int j = 0; j < l; j++) {
                for (int k = 0; k < c; k++) {
                    if (m[j][k] == 'T') {

                        // Direita
                        if (k < c - 1 && m[j][k + 1] == 'A') {
                            temp[j][k + 1] = 'T';
                            isclean = false;
                        }
                        // Esquerda
                        if (k > 0 && m[j][k - 1] == 'A') {
                            temp[j][k - 1] = 'T';
                            isclean = false;
                        }
                        // Cima
                        if (j > 0 && m[j - 1][k] == 'A') {
                            temp[j - 1][k] = 'T';
                            isclean = false;
                        }
                        // Baixo
                        if (j < l - 1 && m[j + 1][k] == 'A') {
                            temp[j + 1][k] = 'T';
                            isclean = false;
                        }
                    }
                }
            }
            m = temp;
        }

        
        for (int z = 0; z < l; z++) {
            for (int x = 0; x < c; x++) {
                cout << m[z][x];
            }
            cout << endl;
        }
        cout << endl;
    }

    return 0;
}
