#include <stdio.h>

int fib1 (int n) ;	//非递归生成下标为n的斐波那契数列元素
int fib2 (int n) ;	//递归生成下标为n的斐波那契数列元素

int main ()
{
	int n ;
	printf ("please input the index of fib:") ;
	scanf ("%d" , &n) ;
	printf ("the %d fib1 number is %d \n" , n , fib1(n)) ;
	printf ("the %d fib2 number is %d \n" , n , fib2(n)) ;
	return 0 ;
}

int fib1 (int n)
{
	int i = 0 ;
	int a = 1 ;
	int b = 1 ;
	int result = 0 ;
	if (n <= 0)
	{
		return 0 ;
	}
	else if (n <= 2)
	{
		return 1 ;
	}
	else
	{
		for (i = 3 ; i <= n ; i ++)
		{
			result = a + b ;
			a = b ;
			b = result ;
		}
		return result ;
	}
}

int fib2 (int n)
{
	if (n <= 0)
	{
		return 0 ;
	}
	else if (n <= 2)
	{
		return 1 ;	//递归终止条件
	}
	else
	{
		return fib2(n-1) + fib2(n-2) ;	//递归
	}
}