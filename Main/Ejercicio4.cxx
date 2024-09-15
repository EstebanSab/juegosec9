#include <iostream>
using namespace std;
int main(int argc, char **argv)
{int Largo, Ancho, Compra;
	cout<<"Ingrese largo de perimetro en metros ";
	cin>>Largo;
	cout<<"Ingrese ancho de perimetro en metros ";
	cin>>Ancho;
	Compra=(Largo+Ancho)*2;
	cout<<"usted debe comprar "<<Compra <<"m de alambre";
	return 0;
}
