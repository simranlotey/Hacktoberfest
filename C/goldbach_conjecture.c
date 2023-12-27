

#include <stdio.h>

int main()
{
    unsigned long long int n,flag,q,jj,flag2,i,j;
    scanf("%llu",&n);
    if (n<=2||n%2!=0){
        printf("Wrong Input");
    }
    else{
        for(i=2;i<=n;i++){
            flag=1;
            for (j=2;j<i;j++){
                if(i%j==0 && i!=j){
                    flag=0;
                    break;
                }
            }
            if(flag==1){
                flag2=1;
                q=n-i;
                for (jj=2;jj<q;jj++){
                    if(q%jj==0 && q!=jj){
                        flag2=0;
                        break;
                    }
                }
                if (flag2==1){
                    printf("%llu+%llu=%llu",i,q,n);
                    break;
                }
            }
        }   
    }
    return 0;
}
