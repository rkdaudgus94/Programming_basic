#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
	bool b1 = true;
	bool b2(false);
	bool b3{ true };
	b3 = false;  // ���������� b3 = 0 ���ش�.

	cout << b1 << endl;  // 1 ���
	cout << std::boolalpha << endl;
	cout << b2 << endl; // "false"�� ���
	cout << b3 << endl; // "false"�� ���
}
