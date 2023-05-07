//
// Created by lds on 23-5-6.
//

#include "../my_header.h"

void createArray() {
    int arr1[3] = {1, 2, 3};
    int arr2[] = {1, 2, 3, 4};
    int arr3[3] = {0};
    int arr4[3] = {};

    cout << "sizeof arr1=" << sizeof(arr1) << endl;
    cout << "sizeof arr2=" << sizeof(arr2) << endl;
    cout << "sizeof arr3=" << sizeof(arr3) << endl;
    cout << "sizeof arr4=" << sizeof(arr4) << endl;

    //情空数组
    memset(arr1, 0, sizeof(arr1));
    //拷贝数组
    int len = sizeof(arr2) / sizeof(int);
    int newArray[len];
    memcpy(newArray, arr2, sizeof(arr2));
    for (int i = 0; i < len; ++i) {
        cout << newArray[i] << " ";
    }
}

//升序回调
int compasc(const void *p1, const void *p2) {
    return *((int *) p1) - *((int *) p2);
}

//降序回调
int compdesc(const void *p1, const void *p2) {
    return *((int *) p2) - *((int *) p1);
}

//二分查找
int binarySearch(int low, int high, int *arr, int target) {
    if (low > high) return -1; //没找到
    int mid = (low + high) / 2;
    if (arr[mid] == target) return mid;
    if (arr[mid] > target) {
        return binarySearch(low, mid - 1, arr, target);
    } else {
        return binarySearch(mid + 1, high, arr, target);
    }
}

void arraySort() {
    int arr[] = {4, 2, 7, 5, 8, 6, 1, 3};

    int len = sizeof(arr) / sizeof(int);
    ::qsort(arr, len, sizeof(int), compasc);

    for (int i = 0; i < len; ++i) {
        cout << arr[i] << " ";
    }
    cout << endl;
}


//string Api测试
void stringApiTest() {
    char str1[] = "abc";
    char str2[] = "def";
    char *dest = strcat(str1, str2);
    cout << "dest = " << dest << endl;
}

int main() {
    //createArray();
    //arraySort();
    int arr[] = {1, 2, 3, 4, 5, 6};
    int index = binarySearch(0, 6, arr, 7);

    cout << "index = " << index << endl;

    stringApiTest();
    return 0;
}
