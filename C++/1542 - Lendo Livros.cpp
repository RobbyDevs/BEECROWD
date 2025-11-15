#include <bits/stdc++.h>
using namespace std;
typedef long long lint;

void solve(int q, int d, int p){

    int ans = (p*d*q)/(p-q);
    cout<<abs(ans);
    
    if (ans ==1)cout<< " pagina\n";
    else cout<< " paginas\n";
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    while (true)
    {
        int q,d,p;
        cin>>q;
        if (q == 0)
            break;
        cin>>d>>p;
        solve(q,d,p);
    }
}
