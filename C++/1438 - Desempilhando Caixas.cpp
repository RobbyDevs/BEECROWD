#include <bits/stdc++.h>

using namespace std;

void solve(int n, int p){
    int inv =0;
    int ans = 0;
    int alt = 0;
    vector <vector<int>> pilhas(p);

    for (int i =0;i<p;i++){

        int t;cin>>t;
        pilhas[i].resize(t);
        for (int j=0;j<t;j++) cin>>pilhas[i][j];

    }
    for (int i =0;i<p;i++){
        for (int j = 0; j<pilhas[i].size();j++){
            if (pilhas[i][j]==1){
                inv = i;
                ans = pilhas[i].size()-j-1;
                alt = j;
            }
        }
    }

    int esq = 0;
    int dir = 0;
    
    for (int i = 0; i<inv; i++) if (pilhas[i].size()>=alt) esq += (pilhas[i].size())-alt;
    for (int i = inv+1; i<p; i++) if (pilhas[i].size()>=alt) dir += (pilhas[i].size())-alt;

    ans += min(esq,dir);

    cout<<ans<<endl;
        

}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    while (true){
        int n,p;
        cin>>n>>p;

        if (n+p == 0) break;
        solve(n,p);
    }
}