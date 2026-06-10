#include<bits/stdc++.h>
using namespace std;
typedef long long ll;


void solve(ll &n, ll &m){

    vector<vector<pair<ll,ll>>>g(n+1);
    vector<ll>vis(n+1);

    priority_queue<
    array<ll,3>,
    vector<array<ll,3>>,
    greater<array<ll,3>>> fila;
    vector<ll>sans(n+1);


    for(ll i=0;i<m;i++){
        ll a,b,c;
        cin>>a>>b>>c;
        g[a].push_back({b,c});
        g[b].push_back({a,c});
    }

    //prim's

    ll p = 1;
    ll ans = 0;
    for(ll i=0;i<=n;i++){
        vis[p] = 1;

        for(pair<ll,ll> x:g[p])
            if (!vis[x.first])
                fila.push({x.second,p,x.first});
        
        while(!fila.empty()){
            array<ll,3>aux = fila.top();

            if (!vis[aux[2]]){
                ans +=aux[0];
                vis[aux[2]] = 1;
                p = aux[2];
                fila.pop();
                sans[aux[1]] = 1;
                sans[aux[2]] = 1;
                break;
            }
            fila.pop();
        }
    }
    ll soma = 0;
    for(ll x:sans)
        if(x)soma++;

    if (soma!= n)
        cout<<"impossivel"<<endl;
    else
        cout<<ans<<endl;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll a,b;
    while (cin>>a>>b)
    solve(a,b);
    
}