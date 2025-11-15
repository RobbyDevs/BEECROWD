#include <bits/stdc++.h>
using namespace std;

void solve(){
    int l,c,m,n,i,j,x,y,s=0,ans=0;
    
    cin>>l>>c>>m>>n;
    
    int ma[l][c];

    for (i=0;i<l;i++)
        for (j=0;j<c;j++)
            cin>>ma[i][j];


    for (i=0;i<l;i+=m)
        for(j=0;j<c;j+=n){
            s = 0;

            for (x=i;x<i+m;x++)
                for(y=j;y<j+n;y++){
                    s+=ma[x][y];

                }
            if(s>ans) ans = s;    
        }   

    
    cout<<ans<<endl;

}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}