//merge two sorted linked list into one sorted linked list
#include<iostream>
using namespace std;

class linkedList {
	struct node{
		node *next;
		int val;
	};
	
	public:
		node *start;
		linkedList();
		~linkedList();
		void insert(int n);
		//void remove();
		void mergesort(linkedList);
		void display();
};

linkedList::linkedList() {
	start=NULL;
}

void linkedList::insert(int n) {
	node *avail, *ptr;
	avail = new node();
	avail->val=n;
	avail->next=NULL;
	if (start==NULL)
		start=avail;
	else {	
		for (ptr=start;ptr->next!=NULL;ptr=ptr->next);
		ptr->next= avail;
	}
}

void linkedList::display() {
	node *ptr;
	for (ptr=start; ptr!=NULL; ptr=ptr->next)
		cout<<ptr->val<<" "	;
}

linkedList::~linkedList(){
}

void linkedList::mergesort(linkedList list2) {
		node *ptr1, *ptr2, *tmp, *start2;
		start2=list2.start;
		//list empty check here;
		if(start->val < start2->val){
			ptr1 =start;
			ptr2 =start2;
			//list2.start=start; does not work coz scope
		}
		else {
			ptr1 =start2;
			ptr2 =start;
			start=list2.start;
		}
		while (ptr1 && ptr2) {
			while(ptr1!=NULL && ptr1->next != NULL && (ptr1->next)->val <= ptr2->val)
				ptr1 =ptr1->next;			
			tmp= ptr1->next;
			ptr1->next=ptr2;
			while(ptr2->next != NULL && tmp!=NULL && (ptr2->next)->val <= tmp->val)
				ptr2=ptr2->next;	
			ptr1=ptr2;
			ptr2=ptr2->next;
			ptr1->next=tmp;
		}
}



int main() {
	linkedList list1, list2;
	int i, n;
	cout<<"\nEnter list1, Enter 0 to stop\n";
	while (1){
		cin>>n;
		if(n==0)
			break;
		list1.insert(n);
	}
	//list1.insert(1);list1.insert(3);list1.insert(6);list1.insert(7);
	cout<<"\nEnter list2, Enter 0 to stop\n";
	while (1){
		cin>>n;
		if(n==0)
			break;
		list2.insert(n);
	}
	//list2.insert(2);list2.insert(4);list2.insert(5);list2.insert(8);
	cout<<"\nList1:\n";
	list1.display();
	cout<<"\nList2:\n";
	list2.display();
	list1.mergesort(list2);
	cout<<"\n\nAfter sort------------------------------";
	//sorted list is the one calling the function. The other list will have part of the sorted list starting from its 'start'
	cout<<"\nList1:\n";
	list1.display();
	cout<<"\nList2:\n";
	list2.display();
	return 0;
}
