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
	cout<<"hay "<<Total <<" alumnos en total";
return 0;
}
