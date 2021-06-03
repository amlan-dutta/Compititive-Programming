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

