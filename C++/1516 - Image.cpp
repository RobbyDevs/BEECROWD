#include <bits/stdc++.h>
using namespace std;

void solve(int l,int c){
    int i,j,z,y,nl,nc,s=0,ans=0;
    string linha;

    char ma[l][c];

    for (i=0;i<l;i++){
        cin>>linha;
        for (j=0;j<c;j++){
            ma[i][j] = linha[j];
            //cout<<linha[j];
        }
    }

    cin>>nl>>nc;
    
    for (i=0;i<l;i++){
        for (z=0;z<(nl/l);z++){
            for (j=0;j<c;j++){
                for (y=0;y<(nc/c);y++)
                    cout<<ma[i][j];
                }
            cout<<endl;
        }
          
    }
    cout<<endl;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int l,c;
    while (true)
    {
        cin>>l>>c;
        if (l+c!=0) solve(l,c);
        else break;
    }
    
}