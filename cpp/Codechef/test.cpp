#include <iostream>
#include <math.h>
#include <string>
#include <vector>
#include <algorithm>
#include <list>
#include <stack>
#include <map>
#include <set>

typedef unsigned long long int ll;

using namespace std;

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int tc = 1;
    //cin >> tc;

    while (tc--)
    {
        int n1, n2, n3;
        cin >> n1 >> n2 >> n3;
        int a1[n1], a2[n2], a3[n3];
        for (int i=0; i<n1;i++)
            cin >> a1[i];
        for (int i=0; i<n2;i++)
            cin >> a2[i];
        for (int i=0; i<n3;i++)
            cin >> a3[i];

        int i=0,j=0,k=0;
        vector <int> final;
        while (i<n1 && j<n2 && k<n3)
        {
            if (a1[i]==a2[j] && a2[j]==a3[k])
            {
                final.push_back(a1[i]);
                i++;
                j++;
                k++;
            }
            else if (a1[i]==a2[j])
            {
                final.push_back(a1[i]);
                i++;
                j++;
            }
            else if (a2[j]==a3[k])
            {
                final.push_back(a2[j]);
                j++;
                k++;
            }
            else if (a1[i]==a3[k])
            {
                final.push_back(a1[i]);
                i++;
                k++;
            }
            else
            {
                if (a1[i]<a2[j] && a1[i]<a3[k])
                    i++;
                else if (a2[j]<a1[i] && a2[j]<a3[k])
                    j++;
                else
                    k++;
            }
        }
        int n = final.size();
        cout << n << endl;
        for (i=0; i < n; i++)
        {
            cout << final[i] << endl;
        }
    }
    return 0;
}



// template <class T>
// T swap(T *a, T *b)
// {
//     T temp = *b;
//     *b = *a;
//     *a = temp;
// };

// class Solution
// {

// public:
//     int *harr;
//     int size;
//     Solution() {}
//     void buildHeap(int a[], int n)
//     {
//         harr = a;
//         size = n;
//         n = (n - 1) / 2;
//         for (int i = n; i >= 0; i--)
//         {
//             heapify(i);
//             // for(int i=0 ; i<size;i++)
//             // {
//             //     cout << harr[i] << ",";
//             // }
//             // cout << "\n";
//         }
//     }
//     void heapify(int idx)
//     {
//         int left = idx * 2 + 1;
//         int right = idx * 2 + 2;
//         int smallest = idx;
//         if (left < size && harr[left] < harr[idx])
//             smallest = left;
//         if (right < size && harr[right] < harr[smallest])
//             smallest = right;
//         if (smallest != idx)
//         {
//             swap(&harr[idx], &harr[smallest]);
//             heapify(smallest);
//         }
//     }
//     int deletemin()
//     {
//         int node = harr[0];

//         if (size > 1)
//         {
//             harr[0] = harr[size - 1];
//             harr[size - 1] = node;
//             size--;
//             heapify(0);
//         }

//         return node;
//     }
//     // arr : given array
//     // l : starting index of the array i.e 0
//     // r : ending index of the array i.e size-1
//     // k : find kth smallest element and return using this function
//     int kthSmallest(int arr[], int l, int r, int k)
//     {
//         //code here
//         buildHeap(arr, r + 1);

//         int ans;
//         for (int i = 0; i < k; i++)
//         {
//             ans = deletemin();
//         }
//         return ans;
//     }
// };

// { Driver Code Starts.

// int main()
// {
// #ifndef ONLINE_JUDGE
//     freopen("input.txt", "r", stdin);
//     freopen("output.txt", "w", stdout);
// #endif

//     int test_case;
//     cin >> test_case;
//     while (test_case--)
//     {
//         int number_of_elements;
//         cin >> number_of_elements;
//         int a[number_of_elements];

//         for (int i = 0; i < number_of_elements; i++)
//             cin >> a[i];

//         int k;
//         cin >> k;
//         Solution ob;
//         cout << ob.kthSmallest(a, 0, number_of_elements - 1, k) << endl;
//     }
//     return 0;
// }
// Driver Code Ends
