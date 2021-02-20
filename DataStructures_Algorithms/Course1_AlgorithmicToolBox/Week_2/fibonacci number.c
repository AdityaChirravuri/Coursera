#include<stdio.h>
#define max 100

int main()
{
    long arr[max];
    int i, n;
    scanf("%d", &n);
    arr[0]=0;
    arr[1]=1;
    if(n==0)
        printf("%ld", arr[0]);
    if(n ==1)
        printf("%ld", arr[1]);
        else{
    for(i=2; i<=n; i++){
        arr[i] = arr[i-1]+arr[i-2];
    }
    printf("%ld", arr[n]);
        }
    return 0;
}
