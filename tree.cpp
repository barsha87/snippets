#include<iostream.h>
#include<conio.h>

class tree
{
      struct node
      {
             char data;
             node *left;
             node *right;
      }*root;
      public:
             tree();
             void ins_node(node *, char d, int ch);
             void insert(node *);
             void inorder(node *);
             void preorder(node *);
             void postorder(node *);
             void disp();
};

void tree::preorder(node *r)
{
     cout<<r->data<<"  ";
     if(r->left !=NULL)
            preorder(r->left);
     if(r->right !=NULL)
            preorder(r->right);
}

void tree::postorder(node *r)
{
     if(r->left!=NULL)
           postorder(r->left);
     if(r->right!=NULL)
           postorder(r->right);
     cout<<r->data<<"  ";
}

void tree::inorder(node *r)
{
     if(r->left !=NULL)
          inorder(r->left);
     cout<<r->data<<"  ";
     if(r->right !=NULL)
          inorder(r->right);
}
     
tree::tree()    
{
     root=new node;
     cout<<"enter element: ";
     cin>>root->data;
     root->left=NULL;
     root->right=NULL;
     insert(root);
}

void tree::ins_node(node *r, char d, int ch)
{
     node *t;
     t=new node;
     t->data=d;
     t->left=NULL;
     t->right=NULL;
     if(ch==1) r->left=t;
     else r->right=t;
}

void tree::insert(node *r)
{
     int ch;
     char d;
     cout<<"\nelement: "<<r->data;
     cout<<"\nenter choice \n1:insert only left child \n2:insert only right child \n3:insert both children \n4:no children\n";
     cin>>ch;
     if(ch==1)
         {
         cout<<"enter left element: ";
         cin>>d;
         ins_node(r, d, ch);
         insert(r->left);
         }
     else if(ch==2)
         {
         cout<<"enter right element: ";
         cin>>d;
         ins_node(r, d, ch);
         insert(r->right);
         }
     else if(ch==3)
         {
         cout<<"enter left element: ";
         cin>>d;
         ins_node(r, d, 1);
         cout<<"enter right element: ";
         cin>>d;
         ins_node(r, d, 2);
         insert(r->left);
         insert(r->right);
         }
}

void tree::disp()
{
     cout<<"\npreorder traversal:\n";
     preorder(root);
     cout<<"\ninorder traversal:\n";
     inorder(root);
     cout<<"\npostorder traversal:\n";
     postorder(root);
}

main()
{
      tree ob;
      ob.disp();
      getch();
}
            
