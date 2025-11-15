#include <bits/stdc++.h>
using namespace std;

int main(){




    long t;
    cin>>t;


    vector <long> id(t);

    for (int w=0;w<t;w++){
        long n;
        cin>>n;
        vector <long> trilhas(n);

        for (int i =0; i<n; i++){
            cin>>trilhas[i];

        }
        long mene=100000,mend=10000;
        
        for (int i = 0; i<n-1;i++){  //---->
            if (trilhas[i]-trilhas[i+1]< mene )
                mene = trilhas[i]-trilhas[i+1];
            
            if ( trilhas[i+1]-trilhas[i] < mend)  //<-----
                mend = trilhas[i+1]-trilhas[i];
        }
        if (mend>mene)
            id[w] = mend;
        else
            id[w] = mene;
        
    }
    for (int j = 0; j<t;j++){
        cout<<id[j]<<endl;
        if (id[j]>=0){
            //cout<<j+1<<endl;

            
        }
    }
}

