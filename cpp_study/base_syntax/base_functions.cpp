//
// Created by lds on 23-5-4.
//
#include "iostream"

using namespace std;

void printTable() {
    for (int i = 1; i <= 9; i++) {
        for (int j = 1; j <= i; j++) {
            cout << j << "*" << i << "=" << i * j << " ";
        }
        cout << endl;
    }
}

int main() {
    printTable();
    return 0;
}