#include <iostream>
 
using namespace std;
 
int main() {
 
    double A = 0, B = 0, MEDIA = 0;

    cin >> fixed;
    cin.precision(1);
    cin >> A;
    cin >> B;



    MEDIA = (A * 3.5 + B * 7.5) / (3.5 + 7.5);

    cout << fixed;
    cout.precision(5);
    cout << "MEDIA = " << MEDIA << endl;

 
    return 0;
}
