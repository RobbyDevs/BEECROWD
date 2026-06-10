#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    ll n; cin>>n;

    vector<pair<ll,ll>>g;
    map<pair<ll,ll>,ll>vis;

    priority_queue<
    array<double,5>,
    vector<array<double,5>>,
    greater<array<double,5>>>fila;


    for(ll i=1;i<=n;i++){
        ll a,b;
        cin>>a>>b;
        g.push_back({a,b});
        vis[{a,b}] = 0;
    }

    //prim's

    double ans = 0;
    pair<ll,ll> x = {g[0].first,g[0].second};
    for(ll i =0; i<n;i++){

        vis[x]=1;

        for(auto y:g){
            if (x!=y && !vis[y]){
                double x1 = x.first;
                double y1 = x.second;
                double x2 = y.first;
                double y2 = y.second;

                double d = sqrt((x2 - x1)*(x2 - x1) +(y2 - y1)*(y2 - y1));
                fila.push({d,x1,y1,x2,y2});
            }
        }

        while(!fila.empty()){
            array<double,5> aux = fila.top();

            if (!vis[{aux[3],aux[4]}]){
                ans += aux[0];
                x = {aux[3],aux[4]};
                fila.pop();
                vis[{aux[3],aux[4]}] = 1;
                break;

            }
            fila.pop();
        }

    }

    ans/=100;
    cout<<fixed<<setprecision(2)<<ans<<endl;

}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll w;cin>>w;
    while(w--)
        solve();
}


//double d = sqrt((x2 - x1)*(x2 - x1) +(y2 - y1)*(y2 - y1));