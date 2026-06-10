#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

ll dfs(ll p, vector<vector<ll>>&g,vector<ll>&vis){

    if (!vis[p]){
        vis[p] = 1;
        for(auto x: g[p]){
            dfs(x,g,vis);
        }

    }
    else
        return 1;

}
void solve(){

    ll n, m;
    cin>>n>>m;

    vector<vector<ll>>g(n+1);
    vector<ll>vis(n+1);

    for(ll i=0;i<m;i++){
        ll a,b;
        cin>>a>>b;
        g[b].push_back(a);
    }

    for(ll i = 0; i<=n;i++){
            
        if (dfs(i,g,vis)){
            cout<<"SIM"<<endl;
            return;
        }
        
    }

    cout<<"NAO"<<endl;
}

int main(){
    ll w;cin>>w;
    while(w--)solve();
}