#include<bits/stdc++.h>
using namespace std;

int main(){
    float a,r;

    cin>>a;

    if(a>2000){

    
        if(a-4500>0){
            r = r+ (a-4500)*0.28;
            a = a-(a-4500);
        }

        if(a-3000.01>0){
            r = r+ (a-3000.01)*0.18;
            a = a-(a-3000.01);
        }
        if(a-2000.01>0){
            r = r+ (a-2000.01)*0.08;
            a = a-(a-2000.01);
        }
        
        cout<<"R$ "<<fixed<<setprecision(2)<<r<<endl;
    
    }

    else{
        cout<<"Isento"<<endl;
    }
}
