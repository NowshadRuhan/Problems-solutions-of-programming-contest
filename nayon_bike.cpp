#include<bits/stdc++.h>
using namespace std;

int main ()
{
    int t;
    cin>> t;
    for(int i=1; i<=t; i++)
    {
        long long p;
        int y, r1, r2;
        cin>>p>>y>>r1>>r2;

        double rate1 = (p*y*(r1/100));
        double rate2 = p*pow((1+(r2/100)),y)-p;
        if(rate1<rate2)
        {
            cout<<"Bank 1"<<endl;
        }else if(rate1>rate2)
        {
            cout<<"Bank 2"<<endl;
        }else{
            cout<<"Confused huh!"<<endl;
        }
    }
    return 0;
}

