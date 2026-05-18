#include<bits/stdc++.h>
using namespace std;
typedef long long ll;


void dfs(char p,map<char,vector<char>>& grafo,map<char,ll>&vis,vector<set<char>>&sans){
    vis[p] = 1;
    sans[sans.size()-1].insert(p);
    for(char x:grafo[p]){
        if(!vis[x]){
            vis[x]=1;
            dfs(x,grafo,vis,sans);
        }
    }
}
ll solve(){
    
    ll ans = 0;
    ll n;ll m;
    cin>>n>>m;
    map<char,vector<char>>grafo;
    vector<set<char>>sans;

    map<char,ll>vis;
    
    string alf = "abcdefghijklmnopqrstuvwxyz";
    for(ll i=0;i<n;i++)
        grafo[alf[i]] = {};
        
    for(ll i=0;i<m;i++){
        char a,b;
        cin>>a>>b;
        vis[a]=0;vis[b]=0;
        grafo[a].push_back(b);
        grafo[b].push_back(a);
    }
    
        
    //dfs
            // a:{b,c,d}

    for(auto x:grafo)
        if (!vis[x.first]){
            sans.push_back({});
            sans[ans].insert(x.first);
            vis[x.first] = 1;
            dfs(x.first,grafo,vis,sans);
            ans++;
        }
    
    //cout<<ans<<endl;

    sort(sans.begin(),sans.end());
    for(auto x:sans){
        for(auto y:x)
            cout<<y<<",";
        cout<<endl;
    }
    return ans;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll w;cin>>w;
    for(ll i=1;i<=w;i++){
        cout<<"Case #"<<i<<":"<<endl;
        cout<<solve()<<" connected components\n\n";
    }
}