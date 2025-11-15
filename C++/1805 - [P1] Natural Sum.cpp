#include <iostream>
using namespace std;
typedef long long lint;

void solve(lint a, lint b){
    lint r;
    r = ((a+b)*((b-a)+1))/2;
    cout<<r<<endl;
}



int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    lint a,b;
    cin>>a>>b;
    solve(a,b);
    return 0;
}