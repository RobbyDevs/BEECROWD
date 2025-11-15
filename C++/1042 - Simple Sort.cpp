#include <bits/stdc++.h>
using namespace std;

int main(){
    
    long a,b,c,maior,meio,menor;

    cin>>a>>b>>c;

    maior = a;
    menor = a;


    if(b>maior)
        maior = b;
    if(c>maior)
        maior = c;

    if(b<menor)
        menor = b;
    if(c<menor)
        menor = c;

    meio = (a+b+c)-(maior+menor);

    
    cout<<menor<<"\n"<<meio<<"\n"<<maior<<endl;

    cout<<"\n"<<a<<"\n"<<b<<"\n"<<c<<endl;

    return 0;



}