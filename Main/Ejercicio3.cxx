#include <iostream>
using namespace std;
int main(int argc, char **argv)
{int primer, segundo;
	float promedio; 
	cout<<"Que nota tenes en tu primer cuatrimetre? ";
	cin>>primer;
	cout<<"Que nota tenes en el segundo cuatrimestre? ";
	cin>>segundo;
	promedio=(primer+segundo)/2.0;
	cout<<"tu promedio es "<<promedio ;
	if(promedio>=7){
		cout<<" aprobado";
	}
	else{
		cout<<" desaprobado";
	}
	return 0;
}
