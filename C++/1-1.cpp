#include<iostream>
#include<stdio.h>
#include<cstdio>

int add(int num_a, int num_b) // 지역 변수로서 함수 실행이 끝나면 사라진다 return을 만나면 num_a, num_b, sum은 사라진다.
{
	int sum = num_a + num_b;
	return sum;
}
//int main()
//{	// 1byte = 8bit
	// int : 자료형(크기 단위, byte) , i : 변수 
	// 정수형 : char(1), short(2), int(4), long(4), long long(8)
	// 실수형 : float(4). double(8)

	//int i = 0;
	//unsigned char c = 0; // 양수만 내포
	


	//return 0;
//}
using namespace std;
int main()
{
	std::cout << add(1, 2) << std::endl;

}