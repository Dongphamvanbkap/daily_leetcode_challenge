#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> replaceElements(vector<int>& arr) {
    
    int n = arr.size();
    for (int i = n-1; i >= 0; i--) {
        if (i != n-1) {
            arr[i] = max(arr[i], arr[i+1]);
        }
    }

    for (int i = 1; i < n; i++) {
        arr[i-1] = arr[i];
    }

    if (n > 0) {
        arr[n-1] = -1;
    }

    return arr;        
}

int main() {
    int arr[] = {17,18,5,4,6,1};
    vector<int> a (arr, arr + sizeof(arr)/sizeof(int));

    vector<int> kq = replaceElements(a);

    for (int i = 0; i < kq.size(); i++) {
        cout << kq[i] << " ";
    }


    return 0;
}