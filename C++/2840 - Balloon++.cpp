#include <bits/stdc++.h>
#include <math.h>
using namespace std;

int main()
{
    double v;
    long long r,l;
    
    cin>>r>>l;
    
    v = (4.0/3.0)*(3.1415)*(pow(r,3));
    v = l/v;


    cout<<v<<endl;
    int re = (int) v;


    cout<<re<<endl;
}