#include<stdio.h>
void main()
{
	char address[10]="1.2.3.4.7";
	int i=0,l=0,j=0;
    
    while(address[i]!='\0')
    {
        if(*(address+i)=='.')
        {
            l++;
        }
        i++;
    }
    char *a=(char*)malloc(i+(2*l)+1);
    i=0;
    while(address[i]!='\0')
    {
        if(address[i]=='.')
        {
            a[j]='[';
            j++;
            a[j]='.';
            j++;
            a[j]=']';
            
        }
        else
        {
            a[j]=address[i];
        }
        i++;
        j++;
    }
    
    a[j]='\0';
    printf("%s",a);
}
