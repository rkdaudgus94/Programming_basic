#include<iostream>

namespace Myspace
{
	int doSomething(int a, int b)
	{
		return a + b;
	}
}

int doSomething(int a, int b)
{
	return a * b;
}

using namespace std;
int main()
{
	cout << doSomething(3, 4) << endl;
}