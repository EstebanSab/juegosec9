#include <iostream>
using namespace std;
int main(int argc, char **argv)
{int Inicio, Final, Antiguedad;
	cout<<"Para saber la antiguedad del trabajador necesiamos primero saber en que año empezo a trabajar en la empresa ";
	cin>>Inicio;
	cout<<"Ahora necesitamos saber hasta que año llevo trabajando en la empresa ";
	cin>>Final;
	Antiguedad=Final-Inicio;
	cout<<"El trabajador tiene "<<Antiguedad <<" años de antiguedad trabajando";
	return 0;
}
