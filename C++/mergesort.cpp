#include<iostream>
using namespace std;

void merge(int a[],int left,int mid,int right){
    int n1 = mid - left + 1;
    int n2 = right - mid;
    int leftarray[n1];
    int rightarray[n2];
    for(int i=0;i<n1;i++){
        leftarray[i] = a[left + i];
    }
    for(int j=0;j<n2;j++){
        rightarray[j] = a[mid + 1 + j];
    }
    int i=0,j=0;
    int k = left;
    while(i<n1 && j < n2){
        if(leftarray[i] <= rightarray[j]){
            a[k] = leftarray[i];
            i++;
        }
        else{
            a[k] = rightarray[j];
            j++;

        }
        k++;

    }
    while(i<n1){
        a[k] = leftarray[i];
        i++;
        k++;
    }
    while(j<n2){
        a[k] = rightarray[j];
        j++;
        k++;
    }
}


void mergesort(int a[],int left,int right){
    if(left < right){
        int mid = (left + right)/2;
        mergesort(a,left,mid);
        mergesort(a,mid+1,right);
        merge(a,left,mid,right);
    }
}

int main(){
    int num;
    cout << "Enter the number of elements: " << endl;
    cin >> num;

    int arr[num];
    cout << "Enter the elements:  " << endl;
    for(int i=0;i<num;i++){
        cin >> arr[i];
    }

    cout << "The unsorted array is: " << endl;
    for(int i=0;i<num;i++){
        cout << arr[i] << "  ";
    }cout << endl;

    mergesort(arr,0,num-1);
    cout << "The sorted array is: " << endl;
    for(int i=0;i<num;i++){
        cout << arr[i] << "  ";
    }

    return 0;
}
