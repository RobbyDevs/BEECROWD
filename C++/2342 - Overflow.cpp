#include <bits/stdc++.h>
using namespace std;

int main(){
    long a,b,r,s;
    string op;

    cin>>s>>a>>op>>b;

    if(op=="*"){
        r = a*b;
    }
    else{
        r = a+b;
    }

    if(s<r){
        cout<<"OVERFLOW"<<endl;
    }
    else{
        cout<<"OK"<<endl;
    }
}