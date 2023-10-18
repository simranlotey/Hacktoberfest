#include <stdio.h>

void FizzBuzz(int data)
{
	for(int i = 1 ; i <= data ; i++)
	{
		if(i % 3 == 0 && i % 5 == 0 )
		  printf(" FizzBuzz ");
		else if(i % 3 == 0)
	    	  printf("Fizz,");
		else if( i % 5 == 0)
		  printf("Buzz,");
		else
			printf("%d," , i);

	}
}
int main()
{
	int limit;
	printf("Enter how many FizzBuzz numbers you want to generate: ");
	scanf("%d" , &limit);
	FizzBuzz(limit);
	return 0;
}
