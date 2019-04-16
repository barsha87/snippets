#include <iostream>
using namespace std;

class QuickUnionUF {
private:
	 int id[10000];
	 int sz[10000];
	 int N;
	 int root(int i);
public:
	  QuickUnionUF(int n);
	  int connected(int p, int q);
	  void Union(int p, int q);
	  void display();
};

QuickUnionUF :: QuickUnionUF(int n)
{
N=n;
for (int i = 0; i < N; i++) 
	{
	id[i] = i;
	sz[i] = 1;
	}
}

int QuickUnionUF :: root(int i)
{
while (i != id[i]) 
	{
	id[i] = id[id[i]];
	i = id[i];
	}
return i;
}

int QuickUnionUF :: connected(int p, int q)
{
 if(root(p) == root(q))
 	return 1;
 else return 0;
}

void QuickUnionUF :: Union(int p, int q)
{
int i = root(p);
int j = root(q);
if (i== j) return;
if (sz[i] <sz[j]) {id[i] =j; sz[j] += sz[i]; }
else				{id[j] =i; sz[i] += sz[j]; }
}

void QuickUnionUF :: display()
{
	int i;
	for(i=0;i<N;i++)
		cout<<id[i] << " ";
	cout<<"\n";
}

class Percolation : public QuickUnionUF {
	private:
		int id[100][100];
		int N;
		int count;
	public:
		 Percolation (int n);
		 void open (int i, int j);
		 int isOpen (int i, int j);
		 int isFull (int i, int j);
		 int percolates ();
		 void disp();
};

Percolation::Percolation(int n) : QuickUnionUF(n*n) {
	count = 1;
	N=n;
	int i,j;
	for(i=0;i<N;i++)
		for(j=0;j<N;j++)
			id[i][j]=-1;
//	QuickUnionUF uf(N*N);		
}

void Percolation::disp(){
	int i,j;
	for(i=0;i<N;i++)
		{
		for(j=0;j<N;j++)
			cout<<id[i][j]<<" ";
		cout<<"\n";
		}
	cout<<"----------FULL---------------\n";
	for(i=0;i<N;i++)
		{
		for(j=0;j<N;j++)
			cout<<isFull(i,j)<<" ";
		cout<<"\n";
		}
}

void Percolation::open(int i, int j) {
	id [i][j] =count;
	count++;
	if (isOpen (i+1,j)) Union(id[i][j], id[i+1][j]);
	if (isOpen (i,j+1)) Union(id[i][j], id[i][j+1]);
	if (isOpen (i-1,j)) Union(id[i][j], id[i-1][j]);
	if (isOpen (i,j-1)) Union(id[i][j], id[i][j-1]);
	if (i == 0) Union(0,id[i][j]);
	if (i == N-1) Union(id[i][j],(N*N)+1);
}

int Percolation::isOpen(int i, int j) {
	if ( 0<=i && i<N && 0<=j && j<N && id[i][j]!=-1 ) return 1;
	return 0;
}

int Percolation::isFull(int i, int j) {
	//int last = (N*N) +1;
	//if (i == last) {
	//cout<<"last";
	//return connected(0,last);
	//}
	//else {
	//cout<<"here";
	return connected(0,id[i][j]);
	//}
}

int Percolation::percolates() {
	return 0;
	return isFull(0,1);
}

int main () 
{
	int N;
	cout <<"Enter N ";
	cin>>N;
	Percolation sys(N);
	int i,j;
	cin>>i;
	while (i!=0)
		{
		cin>>j;
		sys.open(i-1,j-1);
		cin>>i;
		}
	if (sys.percolates() == 1)	cout<<"percolates\n";
	else cout<<"does not percolate\n";
	sys.disp();
}
/*
int main () 
{
	int N;
	cout <<" Enter N ";
	cin>>N;
	QuickUnionUF uf(N);
	uf.Union(4,3);
	uf.Union(3,8);
	uf.Union(6,5);
	uf.Union(9,4);
	cout<<"connected 4,1: "<<uf.connected(4,1)<<"\n";
	uf.Union(2,1);
	uf.Union(5,0);
	uf.Union(7,2);
	uf.Union(6,1);
	uf.Union(7,3);
	cout<<"connected 4,1: "<<uf.connected(4,1)<<"\n";
	uf.display();
}
*/

//fails with only one square; coz 1st n last are automatically connected
//check for cases where i,j are greater than n*n
