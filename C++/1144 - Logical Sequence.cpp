#include <bits/stdc++.h>
using namespace std;

int main(){
    long n, a = 0, b = 1, c = 1, x = 0, y = 0, j = 1;

    cin>>n;

    for (int i = 1; i<=n*2; i++){
        if (i%2 != 0){
            a++;
            b+= x;
            x+=2;
            c+=y;
            y+= j*6;
            
        }
        else{
            b++;
            c++;
            j++;
        }
        cout<<a<<" "<<b<<" "<<c<<endl;
    }
}
