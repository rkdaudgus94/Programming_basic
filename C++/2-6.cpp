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
} // 'abc'를 입력하면 a만 c1에 저장되고 b, c는 버퍼에 남아있게 된다.
