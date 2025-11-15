#include <bits/stdc++.h>
using namespace std;


void solve(){
    int i,j,x,y,flag =0;
    int ma[9][9];
    vector <int> va(9);

    vector <int> v= {1,2,3,4,5,6,7,8,9};

    for (i=0;i<9;i++){
        for(j=0;j<9;j++){
            cin >> ma[i][j];
        }
    }

    for (i=0;i<9;i++){
        vector <int> va(9);
        for (j=0;j<9;j++){
            va[j] = ma[i][j];
        }

        sort(va.begin(),va.end());
        if (va!=v){
            flag = 1;
            break;
        }
    }

    //cout<<flag<<endl;
    
    for (i=0;i<9;i++){
        vector <int> va(9);
        for (j=0;j<9;j++){
            va[j] = ma[j][i];
        }

        sort(va.begin(),va.end());
        if (va!=v){
            flag = 1;
            break;
        }
    }

    if (flag == 1){
        cout<<"NAO"<<endl;
    }

    else{
        for (i=0;i<9;i+=3){
            for (j=0;j<9;j+=3){
                vector <int> va;

                for (x=i;x<(i+3);x++){
                    for (y=j;y<(j+3);y++){
                        va.push_back(ma[x][y]);
                    }
                }
                sort(va.begin(),va.end());
                if (va!=v){
                    flag = 1;
                    break;
                }
                
            }

            if (flag == 1)break;

            
        }
    
        if (flag == 0)cout<<"SIM"<<endl;
        else cout<<"NAO"<<endl;

    }


}
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;cin>>t;
    for (int p = 1;p<t+1;p++){
        cout<<"Instancia "<<p<<endl;
        solve();
        cout<<endl;

    }
    

}
