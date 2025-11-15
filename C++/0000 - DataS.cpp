#include <bits/stdc++.h>
using namespace std;

int main(){
    vector <int> v(10);
    iota(v.begin(),v.end(),1);

    v.pop_back();
    for (auto i:v) cout<<i<<endl;
}