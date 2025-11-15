#include <bits/stdc++.h>
using namespace std;

int main(){
    long w;
    cin>> w;

    for (int ww = 0; ww<w; ww++){
        long n;
        cin>>n;
        vector <long> v;
        for (int i =0; i<n; i++){
            long a;
            cin>>a;
            v.push_back(a);
        }

        sort(v.begin(),v.end());

        cout<<"Case "<<ww+1<<": " <<v[n/2]<<endl;

    

    }
    return 0;
}