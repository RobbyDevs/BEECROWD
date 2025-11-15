#include<bits/stdc++.h>
using namespace std;

int main(){
    int hi,hf,mi,mf,ti,tf,h,m;

    cin>>hi>>mi>>hf>>mf;

    int t = 1440;

    ti = (hi*60)+mi;
    tf = (hf*60)+mf;

    if(tf>ti){
        t = tf-ti;
    }else if(tf<ti){
        t = 1440 - (ti-tf);
    }

    h = (t/60);
    m = (t%60);

    cout<<"O JOGO DUROU "<<h<<" HORA(S) E "<<m<<" MINUTO(S)"<<endl;

    return 0;
    
}