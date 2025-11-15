#include <bits/stdc++.h>
using namespace std;

int main(){
    long a,b,caso=0;
    
    while (true)
    {
        caso +=1;
        cin>>a>>b;
        if (a+b == 0)break;

        vector<int> v(a);

        for (int i =0; i<b;i++){
            long x;
            cin>>x;
            v[x-1]+=1;
            cin>>x;
            v[x-1]+=1;
        }

        long mai = 0;
        cout<<"Teste "<<caso<<endl;
        for (int i:v) if (i>mai) mai = i;

        for (int i = 0; i<a;i++){
            if (v[i] == mai) cout<<i+1<<" ";
        }
        cout<<endl;
        cout<<endl;
    }
    return 0;
    
}