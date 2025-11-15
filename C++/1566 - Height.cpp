#include <bits/stdc++.h>
using namespace std;

int main(){

    long long w,n,a;

    cin>>w;
    for (int i = 0; i<w; i++){
        
        cin>>n;
        vector <int> v;
        vector <int> va;
        
        for (int j = 0; j<n; j++){
            cin>>a;
            va.push_back(a);
        }

        sort(va.begin(),va.end());

        cout<<va[0];
        for(int k=1; k<n;k++){
            cout<<" "<<va[k];
        }
        cout<<endl;
    }

    return 0;



    
}