// BEECROWD N AGUENTA A RECURSÃO
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

int dx[4] = {-1,0,1,0};
int dy[4] = {0,1,0,-1};


void dfs(ll i, ll j,vector<string>& grafo, vector<vector<ll>>& vis){
    
    if (!vis[i][j] && grafo[i][j]=='.'){
        vis[i][j] = 1;
        
        for(ll d = 0; d<4;d++){
            ll x = j + dx[d]; ll y = i + dy[d];

            if (x>=0 && x<grafo[0].size() && y>=0 && y<grafo.size())
                dfs(y,x,grafo,vis);
        }
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0); 
    ll n, m, ans = 0;
    cin>>n>>m;

    vector<string>grafo;
    vector<vector<ll>> vis(n,vector<ll>(m,0));


    for(ll i = 0;i<n;i++){
        string temp; cin>>temp;
        grafo.push_back(temp);
    }

    for(ll i =0;i<n;i++)
        for(ll j = 0;j<m;j++)
            if (!vis[i][j] && grafo[i][j]=='.'){
                dfs(i,j,grafo,vis);
                ans++;
            }

    cout<<ans<<endl;

    return 0;
}