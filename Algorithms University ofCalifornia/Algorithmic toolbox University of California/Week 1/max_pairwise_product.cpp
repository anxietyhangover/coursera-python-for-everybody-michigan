#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
    long i,j,n,a[100000],max,temp;
    cin >> n;
    for( i=0;i<n;i++)
    {
        cin>>a[i];
    }
    max =a[0]*a[1];
    for (i=0;i<n;i++)
    {
        for( j=(i+1);j<n;j++)
        {
            temp = a[i]*a[j];
            if (temp > max) 
            {
                max=temp;
            }
        }
    }
    cout << max;
    return 0;
}