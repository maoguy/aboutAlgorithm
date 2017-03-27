#!/usr/bin/python3
#_*_coding:utf-8_*_

#非递归的方式生成长度为n的斐波那契数列
def createFib1 (n) :
	L = [0] ;
	i , a , b = 0 , 0 , 1 ;
	while i < n :
		L.append (b) ;
		a , b = b , a + b ;
		i = i + 1 ;
	return L ;

#递归的方式生成斐波那契数列中的第n个元素
def fib2 (n) :
	if n <= 0 :
		return 0 ;
	elif n <= 2 :
		return 1 ;
	else :
		return fib2(n-1) + fib2(n-2)

#调用递归函数生成斐波那契数列
def createFib2 (n) :
	L = [] ;
	i = 0 ;
	while i <= n :
		L.append (fib2(i)) ;
		i = i + 1 ;
	return L ;

#generator的方法逐个生成斐波那契数列中的元素
def fib3 (n) :
	yield 0 ;
	i , a , b = 0 , 0 , 1 ;
	while i < n :
		yield b ;
		a , b = b , a + b ;
		i = i + 1 ;

#调用生成器函数生成斐波那契数列
def createFib3 (n) :
	L = [] ;
	for i in fib3(n) :
		L.append (i) ;
	return L ;

#主函数
def main () :
	n = int(input("生成长度为n的斐波那契数列:")) ;
	print ("fib1:") ;
	print (createFib1(n)) ;
	print ("fib2:") ;
	print (createFib2(n)) ;
	print ("fib3:") ;
	print (createFib3(n)) ;

if __name__ == '__main__' :
	main()

