#include <bits/stdc++.h>

using namespace std;

int main(){
    string nome;
    double s,ven;
    cin>>nome>>s>>ven;
    
    cout<<fixed<<"TOTAL = R$ "<<setprecision(2)<<s+(ven*0.15)<<endl;
    return 0;
}