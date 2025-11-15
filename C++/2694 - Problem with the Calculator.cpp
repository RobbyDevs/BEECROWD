#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;

    for(int i = 0; i < n; i++){
        char c[14];
        cin >> c;
        int soma = 0;

        int num = (c[2]-'0')*10 + c[3]-'0';
        int num1 = (c[5]-'0')*100 + (c[6]-'0')*10 + c[7]-'0';
        int num2 = (c[11]-'0')*10 + c[12]-'0';

        soma+=num + num1 + num2;

        cout << soma << endl;
    }
}