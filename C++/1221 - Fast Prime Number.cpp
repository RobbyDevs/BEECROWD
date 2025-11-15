#include <bits/stdc++.h>
using namespace std;

int main(){
    long long w,n,p;

    cin>>w;
    for(int i = 0;i<w;i++)
    {
        int is_prime = 1;
        cin>>n;

        if(n<=1)
        {
            cout<<"Not Prime"<<endl;
            continue;
        }
        else if(n<=3)
        {
            cout<<"Prime"<<endl;
            continue;
            
        }else if(n%2 == 0 || n%3 == 0)
        {
            cout<<"Not Prime"<<endl;
            continue;
        }

        p = 5;

        while(p*p <= n)
        {
            if(n%p==0 || n%(p+2) == 0)
            {
                is_prime = 0;
                break;
            }

            p = p+6;
        }

        if(is_prime == 1)
        {
            cout<<"Prime"<<endl;
            continue;
        }else
        {
            cout<<"Not Prime"<<endl;
            continue;
        }
            
        

    }
    return 0;
}