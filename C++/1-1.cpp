#include<iostream>
#include<stdio.h>
#include<cstdio>

int add(int num_a, int num_b) // ���� �����μ� �Լ� ������ ������ ������� return�� ������ num_a, num_b, sum�� �������.
{
	int sum = num_a + num_b;
	return sum;
}
//int main()
//{	// 1byte = 8bit
	// int : �ڷ���(ũ�� ����, byte) , i : ���� 
	// ������ : char(1), short(2), int(4), long(4), long long(8)
	// �Ǽ��� : float(4). double(8)

	//int i = 0;
	//unsigned char c = 0; // ����� ����
	


	//return 0;
//}
using namespace std;
int main()
{
	std::cout << add(1, 2) << std::endl;

}