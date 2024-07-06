#ifndef INVERSE_KINEMATICS_H
#define INVERSE_KINEMATICS_H

#include <vector>


#define epsilon 1e-6
#define max_iterations 10000

class InverseKinematics {
public:
    InverseKinematics();
    std::vector<double> solve(const std::vector<double>& initial_guess);

private:

    std::vector<double> function(const std::vector<double>& vars);
    std::vector<std::vector<double> > jacobian(const std::vector<double>& vars);
    void compute_functions(const std::vector<double>& vars, std::vector<double>& f);
    void compute_jacobian(const std::vector<double>& vars, std::vector<std::vector<double> >& J);
    std::vector<double> solve_system(const std::vector<std::vector<double> >& J, const std::vector<double>& f);

    double f0(double v0, double v1, double v2, double v3, double v4, double v5);
    double f1(double v0, double v1, double v2, double v3, double v4, double v5);
    double f2(double v0, double v1, double v2, double v3, double v4, double v5);
    double f3(double v0, double v1, double v2, double v3, double v4, double v5);
    double f4(double v0, double v1, double v2, double v3, double v4, double v5);
    double f5(double v0, double v1, double v2, double v3, double v4, double v5);
};

#endif // INVERSE_KINEMATICS_H
