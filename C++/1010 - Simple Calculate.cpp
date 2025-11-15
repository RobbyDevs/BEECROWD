#include <bits/stdc++.h>
using namespace std;

int main(){
    int c1,c2,u1,u2;
    double p1,p2, vt;

    cin>>c1>>u1>>p1;
    cin>>c2>>u2>>p2;

    vt = (u1*p1)+(u2*p2);
    
    cout<<fixed<<"VALOR A PAGAR: R$ "<<setprecision(2)<<vt<<endl;
    return 0;
}