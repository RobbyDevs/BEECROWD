#include <bits/stdc++.h>
using namespace std;

int main(){
    long x,y;
    cin>>x>>y;

    if(x>=0 && x<=432){
        if(y>=0 && y<=468){
            cout<<"dentro"<<endl;
        }
        else{
            cout<<"fora"<<endl;
        }
    }
    else{
        cout<<"fora"<<endl;
    }

}