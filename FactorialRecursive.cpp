#include <iostream>
using namespace std;

int factorial(int a){
  if(a==0){
    return 0;
  }
  if(a<0){
    cout << negative num << endl;
    return 0;
  }
  if(a > 1){
    return  a* factorial(a-1);
  } else {return 1;}
}
int main(){
  int num;
  cin >> num;
  int factorial = factorial(num);
  cout << factorial << endl;
}
