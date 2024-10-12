#include <bits/stdc++.h>

using namespace std;

void insert(stack<int> &st, int n)
{
    if (st.empty() || (st.top() <= n))
    {
        st.push(n);
        return;
    }

    int temp = st.top();
    st.pop();

    insert(st, n);

    st.push(temp);
}

void sortStack(stack<int> &st)
{
    if (st.empty())
    {
        return;
    }

    int t = st.top();
    st.pop();

    sortStack(st);

    insert(st, t);
}

void printStack(stack<int> &s)
{
    while (!s.empty())
    {
        cout << s.top() << " ";
        s.pop();
    }
    cout << endl;
}

int main()
{
    stack<int> st;
    st.push(5);
    st.push(-2);
    st.push(9);
    st.push(-7);
    st.push(3);

    sortStack(st);

    printStack(st);

    while (!st.empty())
    {
        cout << "Stack Top:  " << st.top() << endl;
    }

    return 0;
}