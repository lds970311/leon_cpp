//
// Created by lds on 23-5-4.
//
#include "iostream"

using namespace std;
typedef struct {
    string name;
    int age;
    char *addr;
} Person;

int main() {
    string name;

    cout << "输入姓名：" << endl;
    cin >> name;

    cout << "name=" << name << endl;
    cout << "end" << endl;

    int c = 23.5;
    cout << "c=" << c << endl;

    //C++11初始化赋值
    double d(5.6);
    cout << "d=" << d << endl;
    return 0;
}