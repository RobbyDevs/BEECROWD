#include <bits/stdc++.h>

using namespace std;
int main()
{
    int n;
    float x,y;

    cin>>n;

    for(int i=0;i<n;i++)
    {
        cin>>x>>y;

        if(y==0)
        {
            cout<<"divisao impossivel"<<endl;
        }
        else
        { 
            cout<<fixed<<setprecision(1)<<x/y<<endl;
        }
    }
}