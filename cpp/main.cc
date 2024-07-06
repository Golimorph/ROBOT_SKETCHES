#include "inverseKinematics.h"
#include <iostream>

//./main -10.0 222.2 175.33 1.4707 0 0


int main(int argc, char* argv[]) {
    if (argc != 7) {
        std::cerr << "Usage: " << argv[0] << " x y z alpha beta gamma" << std::endl;
        return 1;
    }

    
    static const double arrDesiredValue[] = {std::stod(argv[1]), std::stod(argv[2]) , std::stod(argv[3]), std::stod(argv[4]), std::stod(argv[5]), std::stod(argv[6])};
    const std::vector<double> desiredValue(arrDesiredValue, arrDesiredValue + sizeof(arrDesiredValue) / sizeof(arrDesiredValue[0]));


    InverseKinematics ik;
    std::vector<double> solution = ik.solve(desiredValue);

    std::cout << "Solution: ";
    for (int i = 0; i<solution.size(); ++i) {
        std::cout << solution.at(i) << " ";
    }
    std::cout << std::endl;

    return 0;
}
