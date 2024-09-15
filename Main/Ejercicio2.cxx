#include <iostream>
using namespace std;
int main(int argc, char **argv)
{int Juan, Maria, Juancopia;
	cout<<"cuantas figuritas tiene Juan? ";
	cin>>Juan;
	cout<<"cuantas figuritas tiene Maria? ";
	cin>>Maria;
	cout<<endl;
	if(Juan==Maria){
		cout<<"Tienen la misma cantidad";
	}
	else{
	Juancopia=Juan;
	Juan=Maria;
	Maria=Juancopia;
	cout<<"Juan tiene "<<Juan<<" figuritas"<<endl;
	cout<<"Maria tiene "<<Maria<<" figuritas";
}
cout<<endl;
system ("pause");
return 0;
}
