#include "inverseKinematics.h"
#include <cmath>
#include <iostream>
#include <stdexcept>

InverseKinematics::InverseKinematics() {}

std::vector<double> InverseKinematics::solve(const std::vector<double>& initial_guess) {
    std::vector<double> vars = initial_guess;
    std::vector<double> f(6);
    std::vector<std::vector<double> > J(6, std::vector<double>(6));

    for (int iter = 0; iter < max_iterations; ++iter) {
        compute_functions(vars, f);
        compute_jacobian(vars, J);

        std::vector<double> delta = solve_system(J, f);

        for (size_t i = 0; i < vars.size(); ++i) {
            vars[i] -= delta[i];
        }

        double norm = 0.0;
        for (int i = 0; i < f.size(); ++i)
        {
            norm += f.at(i) * f.at(i);
        }

        if (std::sqrt(norm) < epsilon) {
            return vars;
        }
    }

    std::cerr << "Newton-Raphson method did not converge\n";

    static const double arr[] = {0, 0, 0, 0, 0, 0};
    return std::vector<double>(arr, arr + sizeof(arr) / sizeof(arr[0]) );
}

void InverseKinematics::compute_functions(const std::vector<double>& vars, std::vector<double>& f) {
    f[0] = f0(vars[0], vars[1], vars[2], vars[3], vars[4], vars[5]);
    f[1] = f1(vars[0], vars[1], vars[2], vars[3], vars[4], vars[5]);
    f[2] = f2(vars[0], vars[1], vars[2], vars[3], vars[4], vars[5]);
    f[3] = f3(vars[0], vars[1], vars[2], vars[3], vars[4], vars[5]);
    f[4] = f4(vars[0], vars[1], vars[2], vars[3], vars[4], vars[5]);
    f[5] = f5(vars[0], vars[1], vars[2], vars[3], vars[4], vars[5]);
}

void InverseKinematics::compute_jacobian(const std::vector<double>& vars, std::vector<std::vector<double> >& J) {
    double h = 1e-8;
    std::vector<double> f1(6), f2(6);

    for (size_t i = 0; i < vars.size(); ++i) {
        std::vector<double> vars1 = vars;
        std::vector<double> vars2 = vars;
        vars1[i] += h;
        vars2[i] -= h;

        compute_functions(vars1, f1);
        compute_functions(vars2, f2);

        for (size_t j = 0; j < 6; ++j) {
            J[j][i] = (f1[j] - f2[j]) / (2 * h);
        }
    }
}

std::vector<double> InverseKinematics::solve_system(const std::vector<std::vector<double> >& J, const std::vector<double>& f) {
    int n = f.size();
    std::vector<double> x(n, 0.0);
    std::vector<std::vector<double> > A = J;
    std::vector<double> b = f;

    for (int i = 0; i < n; ++i) {
        A[i][i] -= b[i];
    }

    // Gaussian elimination
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            double factor = A[j][i] / A[i][i];
            for (int k = i; k < n; ++k) {
                A[j][k] -= factor * A[i][k];
            }
            b[j] -= factor * b[i];
        }
    }

    // Back substitution
    for (int i = n - 1; i >= 0; --i) {
        x[i] = b[i] / A[i][i];
        for (int j = i - 1; j >= 0; --j) {
            b[j] -= A[j][i] * x[i];
        }
    }

    return x;
}


double InverseKinematics::f0(double v0, double v1, double v2, double v3, double v4, double v5) {
    return v0 + v1 + v2 + v3 + v4 + v5 - 1.0;
}

double InverseKinematics::f1(double v0, double v1, double v2, double v3, double v4, double v5) {
    return v0 * v1 * v2 * v3 * v4 * v5 - 1.0;
}

double InverseKinematics::f2(double v0, double v1, double v2, double v3, double v4, double v5) {
    return v0 * v0 + v1 * v1 + v2 * v2 + v3 * v3 + v4 * v4 + v5 * v5 - 1.0;
}

double InverseKinematics::f3(double v0, double v1, double v2, double v3, double v4, double v5) {
    return std::sin(v0) + std::sin(v1) + std::sin(v2) + std::sin(v3) + std::sin(v4) + std::sin(v5) - 1.0;
}

double InverseKinematics::f4(double v0, double v1, double v2, double v3, double v4, double v5) {
    return std::cos(v0) + std::cos(v1) + std::cos(v2) + std::cos(v3) + std::cos(v4) + std::cos(v5) - 1.0;
}

double InverseKinematics::f5(double v0, double v1, double v2, double v3, double v4, double v5) {
    return v0 - v1 + v2 - v3 + v4 - v5;
}