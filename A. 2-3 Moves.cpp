#include<bits/stdc++.h>
using namespace std;

int main ()
{
    int n, t;
    cin>> t;
    for(int i=1; i<=t; i++)
    {
        int m=0, f=0;
        cin>>n;
        if(n==1){
           cout<<2<<endl;
        }else if(n==2){
           cout<<1<<endl;
        }else if(n==3){
           cout<<1<<endl;
        }else if(n==4){
           cout<<2<<endl;
        }else if(n%3 == 0){
            m = (n/3);
            cout<<m<<endl;
        }else if(n%3 == 2){
            m = (n/3);
            m = m+1;
            cout<<m<<endl;
        }else{
            m = (n/3);
            f = (n%3);
            m = m+f;
            cout<<m<<endl;
        }

    }



    return 0;
}

