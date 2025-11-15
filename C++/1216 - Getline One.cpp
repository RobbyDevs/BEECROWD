#include <bits/stdc++.h>
using namespace std;

int main(){
    long c,s,n;
    double r;
    string nome;
    while (getline(cin,nome)){

        if (getline(cin, n)) break;

        cin>>n;
        s = s + n;
        c ++;


    }

    r = s/c;
    cout<<fixed<<setprecision(1)<<r<<endl;
    return 0;

}