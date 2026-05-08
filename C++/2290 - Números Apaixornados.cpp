#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(int n){

    map<ll,ll> mapa;

    vector<ll>v(n);

    for (int i = 0;i<n;i++)cin>>v[i];

    for (int i=0;i<n;i++){
        mapa[v[i]]+=1;
    }
    vector<ll>ans;
    
    for (auto x:mapa){
        //cout<<x.first<<' '<<x.second<<endl;
        if (x.second %2 !=0) ans.push_back(x.first);

    }
    for(auto x : ans)cout<<x<<" ";
    cout<<endl;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    while(true){
        int w;cin>>w;
        if (!w)break;
        solve(w);
    }
}

