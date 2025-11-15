#include <bits/stdc++.h>
using namespace std;

int main(){
    int w; cin>>w;

    while (w--){
        int n; cin>>n;
        set <int> v;

        while (n--)
        {
            int a; cin>>a;
            v.insert(a);
        }

        cout<<(v.size())<<endl;
        


    }
}