#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(){
    ll n,m;
    cin>>n>>m;

    vector<vector<pair<ll,ll>>>g(n+1);
    vector<ll>vis(n+1);

    priority_queue<
    array<ll,3>,
    vector<array<ll,3>>,
    greater<array<ll,3>>>fila;
    

    for (ll i=0;i<m;i++){
        ll a,b,c;
        cin>>a>>b>>c;

        g[a].push_back({b,c});
        g[b].push_back({a,c});
    }
    
    //prim's
    ll ans = 0;
    ll p = 1;

    for (ll i =0;i<=n;i++){
        vis[p] = 1;
        
        for(auto x:g[p]){
            if(!vis[x.first]){
                fila.push({x.second,p,x.first});
            }
        }

        while(!fila.empty()){
            auto aux = fila.top();
            
            if (!vis[aux[2]]){
                vis[aux[2]] = 1;
                p = aux[2];
                ans+=aux[0];
                fila.pop();
                break;
            }
            fila.pop();
        }

    }
    //cout<<">>>>>"<<endl;
    cout<<ans<<endl;
    
    
}