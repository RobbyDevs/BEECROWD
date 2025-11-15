#include <bits/stdc++.h>
using namespace std;

int main(){
    long n,c=0,s;

    cin>>n;
    vector <int> v(n);
    for (int i =0; i<n; i++)
        cin>>v[i];

    if (n==1) cout<<10<<endl;

    else{
        for(int i=0; i<n-1;i++){
            if (v[i+1]-v[i]>=10) c+=10;
            else c+= (v[i+1]-v[i]);
        }
        cout<<c+10<<endl;
    }
}