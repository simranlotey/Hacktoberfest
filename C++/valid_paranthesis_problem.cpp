#include<bits/stdc++.h>
using namespace std;

bool isValid(string s) {
        // approach 1 - using stack
        int n = s.size();
        stack<char> st;
        if(n == 1) return false;
        for(int i = 0 ; i<n ; i++){
            if(s[i] == '(' || s[i] == '[' || s[i] == '{'){
                st.push(s[i]);
            }
            else if((s[i] == ')' && st.empty()) || (s[i] == ']' && st.empty()) || (s[i] == '}' && st.empty())) return false;
            
            else if((s[i] == ')' && st.top() != '(') || (s[i] == ']' && st.top() != '[') || (s[i] == '}' && st.top() != '{')) return false;

            else if((s[i] == ')' && st.top() == '(') || (s[i] == ']' && st.top() == '[') || (s[i] == '}' && st.top() == '{')){
                st.pop();
            }

        }

        if(st.empty()) return true;

        return false;
}
int main(){
    string s = "()()";
    cout<<isValid(s)<<endl;

    return 0;
}