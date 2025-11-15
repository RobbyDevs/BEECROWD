#include <bits/stdc++.h>
using namespace std;

int main(){
    
    vector <int> v = {0,0,0};
    vector <int> v2 ={};
    cin>>v[0]>>v[1]>>v[2];
    string r = "";
    sort(v.begin(),v.end());

    if (v[2] >= v[0]+v[1]){
        r = "n";
    }else{
        if(pow(v[2],2) == (pow(v[0],2))+(pow(v[1],2))){
            r = "r";
        }else if(pow(v[2],2) > (pow(v[0],2))+(pow(v[1],2))){
            r = "o";
        }else if(pow(v[2],2) < (pow(v[0],2))+(pow(v[1],2))){
            r = "a";
        }
    }

    cout<<r<<endl;
}