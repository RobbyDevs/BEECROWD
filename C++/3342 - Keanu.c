#include <stdio.h>
int main()
{
    int n,p,b;
    scanf("%d",&n);

    p = (n*n)/2;
    b = p;
    
    if(n%2 > 0)
        b = b+1;

    printf("%d casas brancas e %d casas pretas\n",b,p);
    return 0;
       
}