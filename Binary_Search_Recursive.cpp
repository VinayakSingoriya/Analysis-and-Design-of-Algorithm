//Recurrence relation => T(n) = { 1     ; n=1
//                              { T(n/2) + 1 ; n>1
//Time complexity : O(logn)


#include <iostream>
#include <cmath>
using namespace std;

int recursive_BinarySearch(int arr[], int low, int high, int key)
{
    if(low==high){
        if(arr[low]==key)
            return low;
        else
            return -1;
    }
    else{
        int mid = floor((low+high)/2);
        if(arr[mid]==key)
            return mid;
        if(key<arr[mid])
            return recursive_BinarySearch(arr, low, mid-1, key);
        else
            return recursive_BinarySearch(arr, mid+1, high, key);       
    }
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
    index = recursive_BinarySearch(arr, 0, size - 1, key);
    if (index != -1)
    {
        cout << "\nElement found at index : " << index;
    }
    else
        cout << "\nElement not found.";

    return 0;
}