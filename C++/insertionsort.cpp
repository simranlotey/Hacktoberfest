#include<iostream>
using namespace std;

void insertionsort(int a[],int n){
    for(int i=0;i<n;i++){
        int key = a[i];
        int j = i - 1;
        while(j>=0 && a[j]>key){
            a[j+1] = a[j];
            j = j-1;
        }
        a[j+1] = key;
    }
}

int main(){
    int n;
    cout << "Enter the number of elements: " << endl;
    cin >> n;

    int a[n];
    cout << "Enter the elements: " << endl;
    for(int i=0;i<n;i++){
        cin >> a[i];
    }

   cout << "The unsorted array is: " << endl;
   for(int i=0;i<n;i++){
        cout << a[i] << "  ";
   }cout << endl;

    insertionsort(a,n);
    cout << "The sorted array is:  " << endl;
    for(int i=0;i<n;i++){
        cout << a[i] << "  ";
    }


    return 0;
}
