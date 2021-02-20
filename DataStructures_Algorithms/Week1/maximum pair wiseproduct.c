#include<stdio.h>

int main()
{
    int arr[100];
    int i, j, n;
    long long min;
    scanf("%d", &n);
    for(i=0; i<n ;i++)
        scanf("%d", arr[i]);
        min =0;
    for(i=0; i<n; i++){
        for(j=i+1; j<n; j++){
            if((long long)arr[i]*arr[j]>min)
                min = (long long)arr[i]*arr[j];
        }
    }
    printf("%lld", min);
    return 0;
}
