#include<iostream>

#define APPLE ;
using namespace std;
int main()
{
	#ifdef APPLE // APPLE�� ���ǵǾ� ���� �� ����
	cout << "APPLE" << endl;
	#endif


	#ifndef APPLE // APPLE�� ���ǵǾ� ���� �ʰų� �ٸ� ���Ͽ� ���� �Ǿ� ������ ����
	cout << "APPLE" << endl;
	#endif
}