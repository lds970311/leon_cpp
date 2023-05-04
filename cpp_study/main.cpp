#include <iostream>

using namespace std;

#define MONTHS 12               // 一年中的月份数。
#define PI              3.14159    // 圆周率。

int main() {
    cout << "Hello, World!" << endl;
    cout << "姓名：" << "西施" << "；年龄：" << 25 << "；体重：" << 48.5
         << "；性别：" << 'X' << endl;

    //声明变量
    string name = "西施";         // 姓名。
    int age = 25;                 // 年龄。
    double weight = 48.6;        // 体重（kg）。
    char sex = 'X';                // 性别：X-女；Y-男。
    bool yz = false;               // 颜值：true-漂亮；false-不漂亮。

    cout << "姓名：" << name << "，年龄：" << age << "，体重：" << weight
         << "，性别：" << sex << "，颜值：" << yz << endl;

    name = "冰冰";           // 字符串有双引号包含。
    age = 23;                // 整数直接书写。
    weight = 50.5;           // 浮点数直接书写。
    sex = 'X';                // 字符用单引号包含。
    yz = true;                // 布尔型取值只能是true和false，或1和0。

    cout << "姓名：" << name << "，年龄：" << age << "，体重：" << weight
         << "，性别：" << sex << "，颜值：" << yz << endl;

    //输出常量值
    cout << "一年有" << MONTHS << "个月。" << endl;
    cout << "圆周率的值是：" << PI << endl;
    return 0;
}
