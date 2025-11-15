#include <bits/stdc++.h>
using namespace std;

const int MAXN=2e6+2;
vector<int>ans(MAXN,0);

vector<int>cprimos(int k){
    vector<int>primo(k+1,1);
    primo[0]=primo[1]=0;
    for(int i=2;i<=sqrt(k);i++){
        if(primo[i]){
            for(int j=i*i;j<=k;j+=i){
                primo[j]=0;
            }
        }
    }
    return primo;
}

void chip(int n){
    vector<int>div(n+1,0);
    for(int i=1;i<=n;i++){
        for(int j=i;j<=n;j+=i){
            div[j]++;
        }
    }
    int max_div=0;
    for(int i=1;i<=n;i++) if(div[i]>max_div)max_div=div[i];
    vector<int>primos_qtd = cprimos(max_div);
    
    int cont=0;
    for(int i=2;i<=n;i++){
        if(primos_qtd[div[i]])cont++;
        ans[i]=cont;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    chip(2e6);
    string s;
    while(getline(cin,s)){
        if(s.empty())break;
        int n=stoi(s);
        cout<<ans[n]<<'\n';
    }
    return 0;
}
