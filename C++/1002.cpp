#include <iostream>
 
using namespace std;
 
int main() {
 
    double R = 0;
    double pi = 3.14159;
    double A = 0;

    cin >> R;

    A = pi *R*R;


    cout << fixed;
    cout.precision(4);
    cout << "A="<< A << endl;
 
    return 0;
}
