#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
ll dl[4] = {0,1,0,-1};
ll dc[4] = {-1,0,1,0};

void pg(vector<vector<ll>>&g){
  for(auto x: g){
    for(auto y:x)cout<<y<<" ";
    cout<<endl;
  }
  cout<<endl;
}

ll dfs(ll i,ll j, vector<vector<ll>>&g, vector<vector<ll>>&vis){
    if (i==4 && j==4)
      return 1;
    
    ll ans = 0;
            
    if(!vis[i][j] && g[i][j] == 0){
      //cout<<i<<" "<<j<<endl;
      
        vis[i][j] = 1;

        for(ll ind = 0;ind<4; ind++){
            ll l = i + dl[ind];
            ll c = j + dc[ind];

            if((l>=0 && l<5)&&(c>=0 && c<5)&&(g[l][c] == 0))
                ans += dfs(l,c,g,vis);
        }

    }
    return ans;

}
void solve(){

    ll n = 5;

    
    vector<vector<ll>>g(5,vector<ll>(5,0));
    vector<vector<ll>>vis(5,vector<ll>(5,0));
    
    for(ll i=0;i<5;i++)
      for(ll j = 0; j<5; j++)
        cin>>g[i][j];
      
      
    //pg(g);

    if (dfs(0,0,g,vis))
        cout<<"COPS"<<endl;
    else
        cout<<"ROBBERS"<<endl;


}

int main(){
    ll w; cin>>w;
    while(w--)solve();
}