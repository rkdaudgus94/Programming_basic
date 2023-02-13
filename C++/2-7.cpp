#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
	int x = 012; // 8진수 : 12 , 10진수 : 1*8 + 2*1 = 10

	int y = 0x12; // 16진수 : 12 , 10진수 1*16 + 2*1 = 18

	int z = 0b1011; // 10진수 : 11 

	int n= 0b1011'1011'1000; // '는 읽지 않음


	const double gravity{ 9.8 }; // #define gravity 9,8보다는 const 구문을 쓰자(헤더 파일에 모아 놓는 게 좋음)

} 
