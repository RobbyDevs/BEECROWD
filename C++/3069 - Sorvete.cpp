#include <bits/stdc++.h>
using namespace std;
typedef long long lint;

int main(){
    
    lint caso = 0;
    while (true){
        caso ++;
        lint s,p;
        cin>>p>>s;
        if (s+p == 0) break;


        vector<vector<lint>> v;

        vector<lint> a(2);
        for (lint i =0; i<s; i++){
            cin>>a[0]>>a[1];
            v.push_back(a);
        }
        sort(v.begin(),v.end());

        cout<<"Teste "<<caso<<endl;

        if (s==1) cout<<a[0]<<" "<<a[1]<<endl;

        else{
            
            vector<vector<lint>> va;
            vector <lint> vv(2);
            
            lint e = v[0][0];
            lint d = v[0][1];

            for (lint i =1; i<s;i++){
                if ((v[i][0] - d) >=1){
                    
                    vv[0] = e;
                    vv[1] = d;
                    va.push_back(vv);
                    e = v[i][0];
                    d = v[i][1];
                }
                else if (d<v[i][1]) d = v[i][1];
            }
            vv[0]=e;
            vv[1]=d;
            va.push_back(vv);
            sort(va.begin(),va.end());
            for (lint i=0; i < va.size();i++){
                cout<<va[i][0]<<" ";
                cout<<va[i][1]<<endl;
            }
            

    
        
        }
        cout<<endl;
    }
}

/*

10 400

80 200
va = []




*/

