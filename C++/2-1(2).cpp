#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
	cout << setprecision(16) << endl; // 출력 스트림에 16자리까지 보장하도록 정보를 낸다
	cout << 1.0 / 3.0 << endl; //16자리까지 보정

	double d1(1.0); // 1
	double d2(0.1 + 0.1 + 0.1 + 0.1 + 0.1+0.1+0.1+0.1+0.1+0.1); // 0.9999999
	// 0.1을 이진수로 표현한 후 더해주기 때문에 딱 떨어지지 못함
	cout << setprecision(17);
	cout << d1 << endl;
	cout << d2 << endl;
}
