#include <bits/stdc++.h>
using namespace std;
int main()
{
    long l,d,k,p,dis,ped;

    cin>>l>>d>>k>>p;

    dis = l*k;
    ped = (l/d)*p;

    cout<<dis+ped<<endl;
}