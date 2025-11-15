#include <bits/stdc++.h>
using namespace std;
int main(){
    for(int i=0;i<2;){

    
        long hi,mi,hf,mf,r,ti,tf;

        cin>>hi>>mi>>hf>>mf;
        
        ti = (hi*60)+mi;
        tf = (hf*60)+mf;
        if(ti+tf == 0){
            break;
        }

        if(tf>ti){
            r = tf-ti;
        }else if(tf < ti){
            r =  1440 - (ti-tf);
        }else{
            r = 1440;
        }
        cout<<r<<endl;
    }
    return 0;
}