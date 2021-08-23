#include <iostream>
#include <iomanip>


int main() 
{
    float variables[6];
    int counter = 0;
    float result = 0;

    for (int i = 0; i < 6; i++)
    {
        std::cin >> variables[i];
    }
    
    for (int i = 0; i < 6; i++)
    {
        if (variables[i] > 0)
        {
            counter++;
            result += variables[i];
        }
    }

    result /= counter;
    std::cout << counter << " valores positivos" << std::endl;
    
    std::cout << std::fixed << std::setprecision(1) << result << std::endl;
}
