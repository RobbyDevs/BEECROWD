#include<bits/stdc++.h>
using namespace std;

void solve(int n, int m) {
    
        vector<vector<pair<int, int>>> ma(n, vector<pair<int, int>>(m));
        vector<pair<int, int>> vr;

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                cin >> ma[i][j].first;
                ma[i][j].second = 0;
            }
        }
        int flag2 = 0;

        
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (ma[i][j].second == 0) {
                    int flag = 0;

                    // Direita
                    if (j < m - 1) {
                        if (ma[i][j + 1].first >= ma[i][j].first) {
                            ma[i][j].second = 1;
                            flag = 1;
                        } else {
                            ma[i][j + 1].second = 1;
                        }
                    }

                    // Baixo
                    if (i < n - 1) {
                        if (ma[i + 1][j].first >= ma[i][j].first) {
                            ma[i][j].second = 1;
                            flag = 1;
                        } else {
                            ma[i + 1][j].second = 1;
                        }
                    }

                    // Esquerda
                    if (j > 0) {
                        if (ma[i][j - 1].first >= ma[i][j].first) {
                            ma[i][j].second = 1;
                            flag = 1;
                        } else {
                            ma[i][j - 1].second = 1;
                        }
                    }

                    // Cima
                    if (i > 0) {
                        if (ma[i - 1][j].first >= ma[i][j].first) {
                            ma[i][j].second = 1;
                            flag = 1;
                        } else {
                            ma[i - 1][j].second = 1;
                        }
                    }

                    // DSD
                    if (i > 0 && j < m - 1) {
                        if (ma[i - 1][j + 1].first >= ma[i][j].first) {
                            ma[i][j].second = 1;
                            flag = 1;
                        } else {
                            ma[i - 1][j + 1].second = 1;
                        }
                    }

                    // DID
                    if (i < n - 1 && j < m - 1) {
                        if (ma[i + 1][j + 1].first >= ma[i][j].first) {
                            ma[i][j].second = 1;
                            flag = 1;
                        } else {
                            ma[i + 1][j + 1].second = 1;
                        }
                    }

                    // DIE
                    if (i < n - 1 && j > 0) {
                        if (ma[i + 1][j - 1].first >= ma[i][j].first) {
                            ma[i][j].second = 1;
                            flag = 1;
                        } else {
                            ma[i + 1][j - 1].second = 1;
                        }
                    }

                    // DSE
                    if (i > 0 && j > 0) {
                        if (ma[i - 1][j - 1].first >= ma[i][j].first) {
                            ma[i][j].second = 1;
                            flag = 1;
                        } else {
                            ma[i - 1][j - 1].second = 1;
                        }
                    }

                    if (flag == 0) {
                        cout<<i+1<<" "<<j+1<<endl;
                        flag2 = 1;
                    }
                }
            }
        }

        if (flag2==0) cout<<-1<<endl;
        cout<<endl;
    
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,m;
    while (cin >> n >> m)
        solve(n,m);
}