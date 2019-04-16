#include <iostream>
#include <string>
using namespace std;

int main() {
	int n=3, i, min_len=500;
	string word[100], the_query;
	cin>>n;
	cin.ignore();
	for(i=0;i<n;i++) {
	getline(std::cin,word[i]);
	if(word[i].length() <min_len)
		min_len=word[i].length();
	}
	getline(std::cin,the_query);
	/*for(i=0;i<n;i++){
		cout<<word[i];
	}
	cout<<the_query;
	*/
	while (the_query.find(" ")!= std::string::npos)
		the_query.replace(the_query.find(" "),1,"");
	//cout<<the_query;
	//j=min_len;
	int j,k;
	for(i=0;i<n;i++){
		j=i;
		k=0;
		while(1){
		//for(j=i;j<n;j++){
			k++;
			while (the_query.find(word[j])!= std::string::npos)
				the_query.replace(the_query.find(word[i]),word[i].length(),"");
			if(j=n-1)
				j=0;
			else
				j++;
			if (k=1) 
				break;
			}
			
			
		if (the_query.length()==0){
			cout<< "matched";
			break;
		}
	
			
	}
	
	
	
}
