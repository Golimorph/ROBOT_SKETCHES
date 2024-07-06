#include "inverseKinematics.h"
#include <iostream>

int main() {
    InverseKinematics ik;

    static const double arr[] = {1.0, 1.0, 1.0, 1.0, 1.0, 1.0};
    std::vector<double> initial_guess(arr, arr + sizeof(arr) / sizeof(arr[0]) );

    std::vector<double> solution = ik.solve(initial_guess);

    std::cout << "Solution: ";
    for (int i = 0; i<solution.size(); ++i) {
        std::cout << solution.at(i) << " ";
    }
    std::cout << std::endl;

    return 0;
}
