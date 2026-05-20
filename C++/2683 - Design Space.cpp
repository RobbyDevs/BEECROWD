#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll m;
    cin>>m;

    vector<vector<pair<ll,ll>>> grafo(1010);
    vector<ll>vis(1010);

    priority_queue<array<ll,3>, vector<array<ll,3>>, less<array<ll,3>>>fila;


    priority_queue< array<ll, 3>, vector<array<ll,3>>, less<array<ll,3>>>filab;

    ll mai= 0;
    for(ll i=0;i<m;i++){
        ll a,b,c;
        cin>>a>>b>>c;
        grafo[a].push_back({b,c});
        grafo[b].push_back({a,c});
        
        mai = max(mai,(max(a,b)));
    }
    ll minAns = 0; ll maxAns = 0;
    ll p=1;
    
    //min

    /**/
    for (ll i=0; i<1010;i++){
        if (i >=mai)break;

        vis[p] = 1;
        for(auto x:grafo[p]){
            if (!vis[x.first])
                fila.push({x.second,p,x.first});

        }

        while(fila.size()){
            auto aux =  fila.top();

            if (2>(vis[aux[1]]+vis[aux[2]])){
                p = aux[2];
                minAns+= aux[0];
                fila.pop();
                break;
            }
            fila.pop();
        }
    }
    vis.assign(1010,0);
    //max
    p = 1;
    for(ll i =0;i<1010;i++){
        if (i >=mai)break;
        vis[p] = 1;
    
        for(auto x:grafo[p])
            if (!vis[x.first])
            filab.push({x.second,p,x.first});
            
        while (filab.size()){
            auto aux = filab.top();
            if (2>(vis[aux[1]]+vis[aux[2]])){
                p = aux[2];
                maxAns += aux[0];
                filab.pop();
                break;
            }
            filab.pop();
        }
            
    }
    cout<<maxAns<<endl;
    cout<<minAns<<endl;
}