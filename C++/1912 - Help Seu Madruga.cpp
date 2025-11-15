#include <bits/stdc++.h>
using namespace std;


double cArea(double corte, vector <int>& v){
    double a = 0;
    for (double i:v){
        if (i>corte) a+= (i-corte);
    }
    return a;
}

void BB(int alvo, double e, double d, double meio, vector<int>& v){
    double area = cArea(meio, v);

    while (abs(area-alvo)>0.00001)    
    {
        if (area < alvo)
            d = meio;
        else{
            if (area > alvo)
                e = meio;
        }
        meio = (e+d)/2;
        area = cArea(meio,v);
    }

    cout<<fixed<<setprecision(4)<<meio<<endl;
    
}

void solve(int n, int a){

    vector <int> v(n);
    long soma = 0;
    int mai = 0;
    for (int i=0;i<n;i++){
        cin>>v[i];
        soma+=v[i];
        if (mai<v[i]) mai = v[i];
    }
    if (soma<a) cout<<"-.-"<<endl;
    else{
        if (soma==a) cout<<":D\n";
        else{
            double esq = 0;
            double dir = mai;
            double meio = (esq+dir)/2;
            BB(a,esq,dir,meio,v);
        }
    }

    
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n,a;
    
    while (true)
    {
        cin>>n>>a;
        if (n+a == 0)break;

        solve(n,a);
    }
    
}