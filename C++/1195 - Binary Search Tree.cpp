#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

void inserir(ll valp, vector<ll>&tree,ll idxp){

    //esq
    if (valp < tree[idxp]){
        
        if(tree[2*idxp]>-1){// ocupado
            inserir(valp,tree,2*idxp);
        }
        else // livre
            tree[2*idxp]=valp;
    }
    //dir
    else{
        if(tree[(2*idxp)+1]>-1){// ocupado
            inserir(valp,tree,(2*idxp)+1);
        }
        else // livre
            tree[(2*idxp)+1]=valp;
    }
}

void pre(ll idxp, vector<ll>&tree){

    cout<<tree[idxp]<<" ";
    if(tree[idxp*2]!=-1){
        pre(idxp*2,tree);
    }
    if(tree[(idxp*2)+1]!=-1){
        pre((idxp*2)+1,tree);
    }
}
void in(ll idxp, vector<ll>&v){

    sort(v.begin(),v.end());
    for(auto x:v)
        if(x>-1)
            cout<<x<<" ";
}

void pos(ll idxp, vector<ll>&tree){

    if(tree[idxp*2]!=-1)
        pos(idxp*2,tree);
    
    if (tree[idxp*2+1]!=-1)
        pos(idxp*2+1,tree);

    cout<<tree[idxp]<<" ";
}

void solve(){
    ll n; cin>>n;
    vector<ll>v(n);
    for(ll i=0;i<n;i++)cin>>v[i];

    

    vector<ll> tree(((100000000)),-1);

    ll idxp = 1;
    tree[1] = v[0];
    
    for(ll i=1;i<n;i++){
        inserir(v[i],tree,idxp);
        cout<<"inserido "<<v[i]<<endl;

    }

    //pv(tree);
    cout<<"Pre.: "; pre(idxp,tree); cout<<endl;

    cout<<"In.: "; in(idxp,v); cout<<endl;

    cout<<"Pos.: "; pos(idxp,tree); cout<<endl;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll w;cin>>w;
    for (ll t=1;t<=w;t++){
        cout<<"Case "<<t<<":"<<endl;
        solve();
        cout<<endl;
    }
}


/*

8 3 10 14 6 4 13 7 1

8-3-10-6-0-14-0-4-0-0-0-13-0-0-0-

*/