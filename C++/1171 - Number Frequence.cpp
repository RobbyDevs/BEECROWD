#include <bits/stdc++.h>
using namespace std;

int main(){
    long n;
    cin>>n;


    vector <long> v(2001);
    for (int w = 0; w<n; w++){
        long x;
        cin>>x;
        v[x-1] +=1;
    }
    for (int i =0; i<2001;i++){
        if (v[i]!= 0){
            cout<<i+1<<" aparece "<<v[i]<<" vez(es)"<<endl;
        }
    }


    
}