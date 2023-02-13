#include<iostream>
using namespace std;
int main()
{
	cout << numeric_limits<float>::lowest() << endl;
	cout << numeric_limits<double>::lowest() << endl;
	cout << numeric_limits<long double>::lowest() << endl;

	float f(3.14);

	cout << 3.14 << endl;
	cout << 31.4e-1 << endl; // 3.14 출력
	cout << 31.4e-2 << endl; // 0.314 출력
	cout << 31.4e1 << endl; // 3.14 출력
	cout << 31.4e2 << endl; // 3.14 출력
}