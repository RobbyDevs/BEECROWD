#include <bits/stdc++.h>
using namespace std;

int main(){
    long w, n, p;
    int prime;

    cin>>w;
    for(int i =0;i<w;i++){
        prime = 1;

        cin>>n;

        if(n<=1){
            cout<<n<<" nao eh primo"<<endl;
            continue;
        }else
        {
            if(n<=3)
            {
            cout<<n<<" eh primo"<<endl;
            continue;
            }

            if(n%2 == 0 || n%3 == 0){
                cout<<n<<" nao eh primo"<<endl;
                continue;
            }
        
        }

        
        p = 5;
        while(p*p<=n){
            if(n%p==0 || n%(p+2)==0){
                prime = 0;
                break;
            }
            p+=6;
        }
        if (prime == 1){
            cout<<n<<" eh primo"<<endl;
            continue;
        }else{
            cout<<n<<" nao eh primo"<<endl;
            continue;
        }

    }
    return 0;
}