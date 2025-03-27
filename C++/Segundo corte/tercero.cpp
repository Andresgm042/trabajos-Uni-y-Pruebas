#include<iostream>
#include<cmath>
using namespace std;

class Vector {
    private:
        float x;
        float y;

    public:
        // Constructor por defecto
        Vector();
        
        // Constructor con parámetros
        Vector(float a, float b);
        
        // Constructor de copia
        Vector(const Vector& v);
        
        // Método para mostrar el vector
        void mostrar();
        
        // Método para calcular el ángulo del vector
        float angulo();
        
        // Establecer el valor de x
        void set_x(float v);
        
        // Establecer el valor de y
        void set_y(float v);
        
        // Método para calcular el módulo del vector
        float magnitud();
        
        // Método para obtener un vector unitario
        Vector unitario();
        
        // Método para multiplicar el vector por un escalar
        Vector multiplicar_escalar(float escalar);
};

// Implementación de los métodos fuera de la clase

// Constructor por defecto
Vector::Vector() : x(0), y(0) {}

// Constructor con parámetros
Vector::Vector(float a, float b) : x(a), y(b) {}

// Constructor de copia
Vector::Vector(const Vector& v) : x(v.x), y(v.y) {}

// Método para mostrar el vector
void Vector::mostrar() {
    cout << '<' << x << ',' << y << '>' << endl;
}

// Método para calcular el ángulo del vector
float Vector::angulo() {
    return atan2(y, x);  // atan2 devuelve el ángulo entre el vector y el eje x
}

// Establecer el valor de x
void Vector::set_x(float v) {
    x = v;
}

// Establecer el valor de y
void Vector::set_y(float v) {
    y = v;
}

// Método para calcular el módulo del vector
float Vector::magnitud() {
    return sqrt(x * x + y * y);
}

// Método para obtener un vector unitario
Vector Vector::unitario() {
    float mag = magnitud();
    if (mag != 0) {
        return Vector(x / mag, y / mag); // Dividimos las componentes del vector entre su módulo
    }
    return Vector(0, 0);  // Si el vector tiene magnitud 0, el vector unitario será 0,0
}

// Método para multiplicar el vector por un escalar
Vector Vector::multiplicar_escalar(float escalar) {
    return Vector(x * escalar, y * escalar);
}

int main() {
    Vector ci(3, 7);  // Vector con componentes (3,7)
    Vector ci2(4,8);

    ci.mostrar();      // Muestra el vector
    ci2.mostrar();

    cout << "Angulo del vector 1: " << ci.angulo() << " radianes" << endl;
    cout << "Angulo del vector 2: " << ci2.angulo() << " radianes" << endl;

    Vector unitario1 = ci.unitario();  // Crea el vector unitario

    cout << "Vector unitario 1: ";
    unitario1.mostrar();               // Muestra el vector unitario

    // Multiplicar el vector por un escalar
    float escalar = 2.0;
    
    Vector escalado = ci.multiplicar_escalar(escalar);
    cout << "Vector 1 multiplicado por " << escalar << ": ";
    escalado.mostrar();
    
    return 0;
}