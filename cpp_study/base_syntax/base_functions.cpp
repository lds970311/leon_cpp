//
// Created by lds on 23-5-4.
//

#include "my_func.h"

int main() {
    //printTable();
    int res = recursionSum(100);

    cout << "res = " << res << endl;

    sizeTest();

//    int a = 015;
//    cout << a << endl;
    string str = R"(
        <no>0001</no>
        <name>西施</name>
        <sc>火树银花</sc>
        <yz>沉鱼</yz>
        <age>23</age>
        <weight>48.5</weight>
        <height>170</height>)";
    cout << str << endl;
    return 0;
}