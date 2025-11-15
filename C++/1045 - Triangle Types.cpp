#include<bits/stdc++.h>
using namespace std;

int main(){
    float a,b,c,maior,meio,menor;

    cin>>a>>b>>c;
    maior = a;
    menor = a;


    if(b>maior)
        maior = b;

    if(c>maior)
        maior = c;
    
    if(b<menor)
        menor=b;

    if(c<menor)
        menor=c;

    meio = (a+b+c)-(maior+menor);

    a = maior;
    b = meio;
    c = menor;

    if(a>=b+c)
        cout<<"NAO FORMA TRIANGULO"<<endl;

    else{
        if(a*a == (b*b)+(c*c))
            cout<<"TRIANGULO RETANGULO"<<endl;
        if(a*a > (b*b)+(c*c))
            cout<<"TRIANGULO OBTUSANGULO"<<endl;
        if(a*a < (b*b)+(c*c))
            cout<<"TRIANGULO ACUTANGULO"<<endl;
 
        if(a == b && b==c)
            cout<<"TRIANGULO EQUILATERO"<<endl;

        if((a==b && a !=c)||(b == c && b!=a))
            cout<<"TRIANGULO ISOSCELES"<<endl;
    }
    

    return 0;
}