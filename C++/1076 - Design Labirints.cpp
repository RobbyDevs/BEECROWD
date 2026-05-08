#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
ll ans = 0;

void dfs(ll p, vector<vector<ll>>&grafo,vector<ll>&vis,ll &ans){
    if(!vis[p]){
        vis[p]=1;
        ans++;

        for(auto x:grafo[p])
            dfs(x,grafo,vis,ans);
    }
}
void solve(){

    ll n,k,p;
    cin>>p>>n>>k;
    vector<vector<ll>>grafo(50);
    vector<ll>vis(50);
    

    for(ll i=0;i<k;i++){
        ll a,b;
        cin>>a>>b;
        grafo[a].push_back(b);
        grafo[b].push_back(a);
    }
    ans = 0;
    dfs(p,grafo,vis,ans);
    ans--;
    cout<<ans*2<<endl;


}
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll w;
    cin>>w;
    while(w--)solve();
}