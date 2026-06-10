#include<bits/stdc++.h>
using namespace std;
typedef long long ll;


void dfs(string p, map<string,vector<string>>&g,map<string,ll>&vis){
    if (!vis[p]){
        vis[p]= 1;

        for(auto x:g[p])
            dfs(x,g,vis);
    }
}

int main(){
    ll n,m;
    cin>>n>>m;

    map<string,vector<string>>g;
    map<string,ll> vis;

    for(ll i=0;i<m;i++){
        string a,b,c;
        cin>>a>>c>>b;

        g[a].push_back(b);
        g[b].push_back(a);
        vis[a] = 0;
        vis[b] = 0;        
    }
    ll ans = 0;
    for(auto x:g){
        if (!vis[x.first]){
            dfs(x.first,g,vis);
            ans++;
        }
    }

    cout<<ans<<endl;
}