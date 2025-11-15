#include<bits/stdc++.h>
using namespace std;
typedef long long lint;

void solve(){
    lint n,ans;cin>>n;
    ans = sqrt(n);
    cout<<n-ans<<endl;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    lint t; cin>>t;
    while (t--)
        solve();
    
    return 0;
}