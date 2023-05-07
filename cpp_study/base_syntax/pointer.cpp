//
// Created by lds on 23-5-5.
//

#include "../my_header.h"

void func(const int *no, const string *str) { // 向超女表白的函数。
    // *no = 8;
    // *str = "我有一只小小鸟。";
    cout << "亲爱的" << *no << "号：" << *str << endl;
}

void memTest() {
    int *pInt = new int(3);
    cout << pInt << endl; //0x55d1831f1eb0
    cout << *pInt << endl; //3

    delete pInt;
}

//二级指针
void secondPtrTest() {
    int i = 8;
    cout << "i=" << i << ",i的地址是：" << &i << endl;
    int *pi = &i;
    cout << "pi=" << pi << ",pi的地址是：" << &pi << ",*pi=" << *pi << endl;
    int **ppi = &pi;
    cout << "ppi=" << ppi << ",ppi的地址是：" << &ppi << ",*ppi=" << *ppi << endl;
    cout << "**ppi=" << **ppi << endl;

}

//函数指针
void handleString(string targetStr, void *handler(string)) {
    handler(targetStr);
}

void caseHandler(const string& target) {
    cout << target << endl;
}

int main() {
    /*int a = 1;
    char b = 'c';
    bool c = false;
    string d = "time";

    cout << "a=" << &a << endl;
    cout << "b=" << &b << endl;
    cout << "c=" << &c << endl;
    cout << "d=" << &d << endl;*/
    memTest();
    secondPtrTest();
    cout << "--------------------" << endl;

    handleString("why are you here?", reinterpret_cast<void *(*)(string)>(caseHandler));
    return 0;
}