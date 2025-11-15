#include <bits/stdc++.h>
using namespace std;


void LIS(){
    int n;
    while (cin >> n) {
        vector<long> pilhas;

        for (int i = 0; i < n; i++) { 
            long val; 
            cin >> val;

            if (pilhas.empty()) {
                pilhas.push_back(val);
            }
            
            int e = 0;
            int d = pilhas.size();

            while (e < d) { // busca binaria para achar o menor valor maior que v[i]
                int m = (e+d)/2;

                if (pilhas[m] < val)
                    e = m + 1;
                else
                    d = m;
            }

            if (e == pilhas.size()) //nao achou o valor, adiciona val na pilha
                pilhas.push_back(val);
            else
                pilhas[e] = val;// achou, substitui pilha[e] por val
            }
            cout<<pilhas.size()<<endl;
        }
}
        

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    LIS();
}