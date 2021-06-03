#include<iostream>
#include <math.h>
#include <string>
#include <vector>
#include <algorithm>
#include <list>
#include <stack>
#include <map>
#include <set>

#define PI 3.1415926535897932384626433832795
#define MOD 1000000007
#define INF (int)1e9

typedef unsigned long long int ll;

using namespace std;

int main()
{
    #ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif

	int tc;
	cin >> tc;

	while(tc--){
        ll n;
		cin >>n;
        while(true)
        {
            ll digitSum=0;
            ll n_copy=n;
            while (n_copy>0)
            {
                digitSum+=n_copy%10;
                n_copy=n_copy/10;
            }
            if (__gcd(n,digitSum)!=1) 
            {
                cout << n <<endl;
                break;
            }
            n++;
        }
	}
	return 0;
}
