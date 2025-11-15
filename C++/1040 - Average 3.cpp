#include <bits/stdc++.h>
using namespace std;

int main(){
    float a,b,c,d,e,r;


    cin>>a>>b>>c>>d;

    r = ((a*2)+(b*3)+(c*4)+d)/(10);

    
    cout<<fixed<<setprecision(1)<<"Media: "<<r<<endl;
    if(r>=7){
        cout<<"Aluno aprovado."<<endl;
    }
    else{
        
        if(r<5){
            cout<<"Aluno reprovado."<<endl;

        }
        else{
            cout<<"Aluno em exame."<<endl;

            cin>>e;
            r = (r+e)/2;
            cout<<"Nota do exame: "<<fixed<<setprecision(1)<<e<<endl;

            if(r>=5){
                cout<<"Aluno aprovado."<<endl;
            }else{
                cout<<"Aluno reprovado."<<endl;
            }


            cout<<"Media final: "<<fixed<<setprecision(1)<<r<<endl;



        }


    }
    return 0;
}