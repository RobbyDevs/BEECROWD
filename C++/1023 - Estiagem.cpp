#include <bits/stdc++.h>
using namespace std;
typedef long long lint;

void solve(int t,int cidade){
    cout<<"Cidade# "<<cidade<<":\n";
    vector<int> freq(201);
    int c = 0, p = 0;
    for(int w=0;w<t;w++){
        int x,y;
        cin>>x>>y;
        
        freq[y/x]+=x;
        c+=y;
        p+=x;
        
    }

    for (int j=0;j<freq.size();j++){
        if (freq[j]>0){
            cout<<freq[j]<<"-"<<j;
            if (j<freq.size()-1)
                cout<<" ";
        }
        
    }
    cout<<endl;
    float f = static_cast<float>(c)/p;
    ostringstream o;
    o << fixed<<setprecision(3)<<f;
    string ff = o.str();
    ff.pop_back();
    
    cout<<"Consumo medio: "<<ff<<" m3.\n";

}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int cidade = 0;
    while (true)
    {
        
        int w;
        cin>>w;
        if (w==0) break;
        cidade ++;

        //cout<<"Cidade# 1:\n";
        solve(w,cidade);
        cout<<endl;
    }
    return 0;
    
}