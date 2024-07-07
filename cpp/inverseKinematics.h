#ifndef INVERSE_KINEMATICS_H
#define INVERSE_KINEMATICS_H

#include <vector>

#define A1  40.86
#define A2  44.83
#define B  123.0
#define C1  17.5
#define C2  131.34
#define D1  20 //need to measure
#define D2  20 //need to measure
#define E1  20 //need to measure
#define E2  10 //need to measure
#define F1  10 //need to measure
#define F2  10 //need to measure

#define epsilon 1e-4
#define max_iterations 1000

class InverseKinematics 
{
public:
    InverseKinematics();
    bool solve(const std::vector<double>& desiredValue, std::vector<double>& solution);

private:

	void compute_functions(const std::vector<double>& vars, std::vector<double>& funcs);
    void compute_jacobian(const std::vector<double>& vars, std::vector<std::vector<double> >& J);
    std::vector<double> solve_system(const std::vector<std::vector<double> >& J, const std::vector<double>& funcs);

    bool solveForGuess(std::vector<double>& solution, std::vector<double> guess);

    std::vector<double> m_desiredValue;
    std::vector<double> m_lastSolution;


    //tabulate som known solutions that can be used as initial guesses: 



};



#endif // INVERSE_KINEMATICS_H
