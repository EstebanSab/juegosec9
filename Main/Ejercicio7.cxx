#include <iostream>
#include <math.h>
using namespace std;
int main(int argc, char **argv)
{int Lado;
	string Metros;
	cout<<"Para saber el area de un cuadrado necesitamos saber cuanto mide un lado del mismo: ";
	cin>>Lado;
	cout<<"Se mide en cm, km, mm o Metros: ";
	cin>>Metros;
	cout<<"El cuadrado tiene "<< pow(Lado,2) << Metros<< " cuadrados de area";
	return 0;
}

