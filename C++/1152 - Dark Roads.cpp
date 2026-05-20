#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(ll n, ll m){

    ll ans = 0;
    ll soma = 0;

    vector<vector<pair<ll,ll>>> grafo(n);
    priority_queue<vector<ll>> fila;
    vector<ll>vis(n);
    
    for(ll i=0;i<m;i++){
        ll a,b,c;
        cin>>a>>b>>c;
        grafo[a].push_back({b,c});
        grafo[b].push_back({a,c});
        soma+=c;
    }
    ll p=0;

    for(ll i=0;i<n;i++){
        
        for(auto x: grafo[p]){
            vis[p]=1;
            fila.push({-x.second,p,x.first});
        }

        while(fila.size()){
            vector<ll> aux = fila.top();

            if (2>(vis[aux[1]]+vis[aux[2]])){
                p = aux[2];
                ans+= abs(aux[0]);
                fila.pop();
                break;
            }
            else
                fila.pop();
        }

    }
    cout<<soma-ans<<endl;

}


int main(){

    while(true){
        ll n,m;
        cin>>n>>m;
        if (!(n+m))break;

        solve(n,m);
    }
}