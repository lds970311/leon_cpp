//
// Created by lds on 23-5-4.
//

#include "my_func.h"

void printTable() {
    for (int i = 1; i <= 9; i++) {
        for (int j = 1; j <= i; j++) {
            cout << j << "*" << i << "=" << i * j << " ";
        }
        cout << endl;
    }
}

/**
 * 递归求和
 * @param num
 * @return 求和后的 值
 */
int recursionSum(int num) {
    if (num == 0) return 0;

    return num + recursionSum(num - 1);
}

void sizeTest() {
    // 用于数据类型：sizeof(数据类型)
    // 用于变量：sizeof(变量名) 或 sizeof 变量名
    // C++常用的数据类型：整数（int）、浮点数（float和double）、字符（char）和布尔（bool）。
    cout << "sizeof(int)=" << sizeof(int) << endl;
    cout << "sizeof(float)=" << sizeof(float) << endl;
    cout << "sizeof(double)=" << sizeof(double) << endl;
    cout << "sizeof(char)=" << sizeof(char) << endl;
    cout << "sizeof(bool)=" << sizeof(bool) << endl;
    cout << "sizeof(long long)=" << sizeof(long long) << endl;
    cout << "sizeof(long double)=" << sizeof(long double) << endl;

    int i;
    cout << "sizeof(int)=" << sizeof i << endl;
    float f;
    cout << "sizeof(float)=" << sizeof f << endl;
    double d;
    cout << "sizeof(double)=" << sizeof d << endl;
    char c;
    cout << "sizeof(char)=" << sizeof c << endl;
    bool b;
    cout << "sizeof(bool)=" << sizeof b << endl;
}