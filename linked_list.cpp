#include<iostream>
using namespace std;
class list{
      struct node{
         string data;
         node* link;
         }*start;
      public:
             list();
             void insert(string);
             void del();
             void display();
      };

list::list(){
     start=NULL;
     }
     
void list::insert(string str){
     node *avail, *p;
     avail=new node;
     avail->data=str;
     avail->link=start;
     start=avail;
     }
     
void list::del(){
     node *p;        
     p=start;
     start=start->link;
     delete p;
     }

void list::display(){
     node*p;
     for(p=start;p->link!=NULL;p=p->link)
        cout<<p->data<<" -> ";
     cout<<p->data<<endl;
     }
     
int main()
{
    list list1;
    list1.insert("Hi");
    list1.display();
    list1.insert("awesome");
    list1.display();
    list1.insert("list");
    list1.display();
    list1.insert("nice");
    list1.display();
    list1.del();
    list1.display();
    list1.del();
    list1.display();
    list1.del();
    list1.display();
}
    

