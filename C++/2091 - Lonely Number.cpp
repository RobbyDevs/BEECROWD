#include <bits/stdc++.h>
using namespace std;
typedef long long lint;

int main(){
    lint t,w,i,n;


    while (true){
        cin>>n;

        if (n==0) break;

        map<lint,lint> dic;

        for(w=0;w<n;w++){
            lint i;
            cin>>i;
            dic[i]+=1;
        }
        
        for (auto [chave,valor]:dic){
            if (valor%2 != 0){
                cout<<chave<<endl;
                break;
            }
        }

    }

}