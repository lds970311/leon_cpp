// cpp条件分支

#include "iostream"

using namespace std;

int main() {
    // 超女的身材：1-火辣；2-丰满；3-苗条；4-强壮；5-肥胖；>5-未知 。

    // 声明存放超女身材数据的变量。
    int sc;

    // 显示“请输入身材的代码（1-火辣；2-丰满；3-苗条；4-强壮；5-肥胖；>5-未知）：”的提示文字。
    cout << "请输入身材的代码（1-火辣；2-丰满；3-苗条；4-强壮；5-肥胖；其它表示未知）：";

    // 输入超女身材的代码，存放在变量中。
    cin >> sc;

    // 用多条件的if语句，判断身材代码，显示身材的中文描述。
    if (sc == 1) cout << "火辣!\n";
    else if (sc == 2) cout << "丰满!\n";
    else if (sc == 3) cout << "苗条!\n";
    else if (sc == 4) cout << "强壮!\n";
    else if (sc == 5) cout << "肥胖!\n";
    else cout << "未知!\n";
    return 0;
}