#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cout<<"Enter the size(odd integer): ";
    cin>>n;
    int s=n/2;
    int f=1;
    while(f<=n){{
        for(int i=0;i<s;i++){
            cout<<" ";
        }
        for(int i=0;i<f;i++){
            cout<<"*";
        }
        cout<<endl;
        s--;f+=2;
    }

    }
    return 0;
}

