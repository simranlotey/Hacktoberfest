#include<iostream>
using namespace std;
class node{
    public:
    int data;
    node* left;
    node* right;
};
node* newNode(int value)
{
    node* temp = new node;
    temp -> data = value;
    temp->left=NULL;
    temp->right=NULL;
    return temp;
}
int height(node* root)
{
    if(root==NULL)
    return 0;
    else {
        int l = height(root->left);
        int r = height(root->right);

        if(l>r)
        return l+1;
        else
        return r+1;
    }
}
int main()
{
    node* root = newNode(0);
    root -> left = newNode(1);
    root -> right = newNode(2);
    root -> left ->left = newNode(3);
    root -> left -> right = newNode(4);
    root -> right -> left = newNode(5);
    root -> right -> right = newNode(6);
    root -> right -> right -> left = newNode(7);

    int h = height(root);
    cout  << h;
    return 0;
}