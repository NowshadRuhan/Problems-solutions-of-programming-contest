#include<bits/stdc++.h>
using namespace std;
int prime_or_not(int n) {

    int i, m=0, flag=0;
    m=n/2;
    for(i = 2; i <= m; i++)
    {
        if(n % i == 0)
        {
            return 2;
            flag=1;
            break;
        }
    }
    if (flag==0) return 1;
}

int main ()
{
    int n, values;
    string name;
    cin>> n;
    for(int i=1; i<=n; i++)
    {
        cin>>name;
        cin>>values;

        int length = name.length();
        //cout<<length << values<<endl;
        int f =0;
        for(int j=0; j<name.length(); j++)
        {
            int val = (int)name[j];
             //cout<<val<<endl;
            val = val + values;
            int result = prime_or_not(val);

            if(result == 1)
            {
                f =1;
                printf("YES\n");
                break;
            }else{
                //printf("NO\n");
            }
            //cout<<val<<endl;
        }
        if(f == 0){
            printf("NO\n");
        }


    }


    return 0;
}
