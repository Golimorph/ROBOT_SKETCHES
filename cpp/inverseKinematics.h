#ifndef INVERSE_KINEMATICS_H
#define INVERSE_KINEMATICS_H

#include <vector>

#define A1  41.85 //OK
#define A2  44.79 //OK
#define B  129.9 //OK
#define C1  17.6 //OK
#define C2  122.45 //OK 
#define D1  6.41 //need to measure
#define D2  43.57 //need to measure
#define E1  39.51 //need to measure
#define E2  8.28 //need to measure
#define F1  19.2 //need to measure
#define F2  71.53 //need to measure

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


    /*! @brief normalize the solution to within -M_PI to M_PI */
    void normalize(std::vector<double> &solution);


    /*! @brief check if the presented solution is within the abilities of the robot arm 
     * @paramm solution the solution to check
     * @return true if the solution is possible for the robot arm.*/
    bool isValid(const std::vector<double>& solution);

    bool solveForGuess(std::vector<double>& solution, const std::vector<double> guess);

    std::vector<double> m_desiredValue;
    std::vector<double> m_lastSolution;

    //min_a,max_a,...,min_f,max_f
    std::vector<double> m_limits;


    //tabulate som known solutions that can be used as initial guesses: 



};



#endif // INVERSE_KINEMATICS_H
