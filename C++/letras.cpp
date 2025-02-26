#include <iostream>
#include <string>
#include <sstream>

void fun(string a, int b [], int 8c) 
	int j=1;  b[0]=a.at(0);
	
	for (int i=0; i<a.lenght(); i++){
		if (a.at(i) == ' '){
			b[j] = a.at(i+1);
			j++;
		}
		
		c=j;
	}


int main (){
	string frase, int k;
	
	cout << "Digite la frase: " << endl;
	
	getline(cin, frase);
	char arr[] = {};
	funcion(frase, arr &k);
	
	for (int i = 0, i<frase.lenght(); i++){
		cout << arr[i]<<' ';
	}
	
	return 0;
}
