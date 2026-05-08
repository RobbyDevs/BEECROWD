#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(ll n, ll k){
    
    vector<vector<pair<ll,ll>>> grafo(n);
    priority_queue<ll>fila;

    for(ll i=0;i<n;i++){
        ll a,b,c;
        cin>>a>>b>>c;
        grafo[a].push_back({b,c});
        grafo[b].push_back({a,c});
    }

    sort(grafo.begin(),grafo.end());

    // Robert Prim

    for(ll )


}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    ll w;cin>>w;
    while (true){
        ll n,k;
        cin>>n>>k;
        if (!(n+k))break;

        solve(n,k);
    }
}