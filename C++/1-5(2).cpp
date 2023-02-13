#include<iostream>

#define APPLE ;
using namespace std;
int main()
{
	#ifdef APPLE // APPLE이 정의되어 있을 시 실행
	cout << "APPLE" << endl;
	#endif


	#ifndef APPLE // APPLE이 정의되어 있지 않거나 다른 파일에 정의 되어 있으면 실행
	cout << "APPLE" << endl;
	#endif
}