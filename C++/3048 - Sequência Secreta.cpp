#include <bits/stdc++.h>
using namespace std;

int main(){
    long n,x,ant=0,c=0;

    cin>>n;
    vector <long> v(n);
    for (long i = 0; i<n; i++){
        cin>>v[i];
    }

    for (long i:v)
        if (i!=ant){
            ant = i;
            c++;
        }
    cout<<c<<endl;
    return 0;

}