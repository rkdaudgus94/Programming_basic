#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
	char c1(65);

	cin >> c1;
	cout << c1 << " " << static_cast<int>(c1) << endl;

	cin >> c1;
	cout << c1 << " " << static_cast<int>(c1) << endl;
} // 'abc'�� �Է��ϸ� a�� c1�� ����ǰ� b, c�� ���ۿ� �����ְ� �ȴ�.
