#include <bits/stdc++.h>
using namespace std;


void solve(int caso, int n, int q){
    cout<<"CASE# "<<caso<<":\n";

    vector<int> v(n);
    for (int i = 0;i<n;i++)cin>>v[i];

    int mai=v[0],men=v[0],dif;

    for (auto i:v){
        if(i>mai) mai = i;
        if(i<men)men=i;
    }
    dif = mai-men+1;

    vector<int>vf(dif+1);

    for(int i:v) vf[i-men]+=1;

    vector<int> vp(dif+2,0);

    for (int i = 1; i< dif+2;i++)
        vp[i] = vp[i-1]+vf[i-1];
    
    for(int x=0; x<q;x++){
        int alv=0; cin>>alv;
        if ((alv<men) || (alv>mai) || (vf[alv-men]==0))
            cout<<alv<<" not found\n";
        else{
            int pos = vp[alv-men]+1;
            //cout<<vp[alv-men]<<endl;
            cout<<alv<<" found at "<<pos<<endl;
        }
    }

}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int caso=0,n,q;

    while(true){
        caso++;
        cin>>n>>q;
        if (n+q == 0) break;

        solve(caso,n,q);
    }
}