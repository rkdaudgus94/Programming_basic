#include<iostream>

void f();
int main()
{
    f(); // 정의는 뒤에있더라도 이제 무슨 함수인지 앞에서 알게 됨
}
void f()
{
    std::cout << "love" << std::endl;
}