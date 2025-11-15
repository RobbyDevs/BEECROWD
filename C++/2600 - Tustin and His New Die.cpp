#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;

    for (int w = 0; w<n; w++){

        vector <int> v;
        int val;

        for(int i = 0; i<6; i++){
            cin >> val;
            v.push_back(val);
        }

        vector <int> vb = v;
        sort(begin(vb),end(vb));

        vector <int> va{1,2,3,4,5,6};
        if (vb == va){
            if (v[0]+v[5]==7 && v[1]+v[3]==7 && v[2]+v[4]==7)
                cout<<"SIM"<<endl;
            else cout<<"NAO"<<endl;
            
        }
        else cout<<"NAO"<<endl;
        //ASPAS DUPLHAS. DROGA.
    }
}