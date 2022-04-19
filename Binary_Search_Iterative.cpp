//min comparison : 1 (When element is at the mid initially) => O(1)
//max comparison : log(n) =>O(logn)


#include <iostream>
#include <cmath>
using namespace std;

int iterative_BinarySearch(int arr[], int low, int high, int key)
{
    while (low <= high)
    {
        int mid = floor((low + high) / 2);
        if (key == arr[mid])
            return mid;
        if (key < arr[mid])
            high = mid - 1;
        else
            low = mid + 1;
    }
    return -1;
}

int main()
{
    int size, val, index, key;
    cout << "Enter size of array : ";
    cin >> size;
    int arr[size];
    for (int i = 0; i < size; i++)
    {
        cin >> val;
        arr[i] = val;
    }
    cout << "\nKey : ";
    cin >> key;
    index = iterative_BinarySearch(arr, 0, size - 1, key);
    if (index != -1)
    {
        cout << "\nElement found at index : " << index;
    }
    else
        cout << "\nElement not found.";

    return 0;
}