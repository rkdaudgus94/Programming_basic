#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
	bool b1 = true;
	bool b2(false);
	bool b3{ true };
	b3 = false;  // 내부적으로 b3 = 0 해준다.

	cout << b1 << endl;  // 1 출력
	cout << std::boolalpha << endl;
	cout << b2 << endl; // "false"로 출력
	cout << b3 << endl; // "false"로 출력
}
