#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
	cout << setprecision(16) << endl; // ��� ��Ʈ���� 16�ڸ����� �����ϵ��� ������ ����
	cout << 1.0 / 3.0 << endl; //16�ڸ����� ����

	double d1(1.0); // 1
	double d2(0.1 + 0.1 + 0.1 + 0.1 + 0.1+0.1+0.1+0.1+0.1+0.1); // 0.9999999
	// 0.1�� �������� ǥ���� �� �����ֱ� ������ �� �������� ����
	cout << setprecision(17);
	cout << d1 << endl;
	cout << d2 << endl;
}
