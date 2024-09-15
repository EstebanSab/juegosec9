#include <iostream>
using namespace std;
int main(int argc, char **argv)
{int Sociales, Naturales, Economia, Total;
	cout<<"cuantos alumnos hay en Sociales? ";
	cin>>Sociales;
	cout<<"cuantos alumnos hay en Naturales? ";
	cin>>Naturales;
	cout<<"cuantos alumnos hay en Economia? ";
	cin>>Economia;
	Total=Sociales+Naturales+Economia;
	cout<<"hay "<<Total <<" alumnos en total"<<endl<<endl;
	cout<<endl;
	if(Naturales>Sociales && Naturales>Economia){
		cout<<"Naturales tiene mas alumnos";
	}
	else{
		if(Sociales>Economia && Sociales>Naturales){
			cout<<"Sociales tiene mas alumnos";
		}
		else{
				if(Naturales==Sociales or Naturales==Economia or Sociales==Economia){
            		cout<<"hay 2 o mas cursos con la misma cantidad";
	             } 
                  else{
			cout<<"Economia tiene mas alumnos";
		     }
		}}
cout<<endl;		
system ("pause");
return 0;
}

