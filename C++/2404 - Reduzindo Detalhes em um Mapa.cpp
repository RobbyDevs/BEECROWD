#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    ll n, m;
    cin>>n>>m;

    vector<vector<pair<ll,ll>>>grafo(n+1);
    vector<ll>vis(n+1);
    priority_queue<vector<ll>>fila;


    for(ll i=0;i<m;i++){
        //cout<<">>>\n";
        ll a,b,c;
        cin>>a>>b>>c;
        grafo[a].push_back({b,c});
        grafo[b].push_back({a,c});
    }

    ll p = 1;
    ll ans = 0;
    
    for(ll i=1;i<=n;i++){
        
        for(auto x:grafo[p]){
            vis[p]=1;
            
            fila.push({-x.second,p,x.first});
        }

        while(fila.size()){
            vector<ll> aux = fila.top();

            if (2>vis[aux[1]]+vis[aux[2]]){
                p = aux[2];
                ans+= abs(aux[0]);
                fila.pop();
                break;
            }
            else
                fila.pop();

        }
    }
    cout<<ans<<endl;


}