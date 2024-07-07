#include "inverseKinematics.h"
#include <iostream>

//./main -10.0 222.2 175.33 1.4707 0 0

/*
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
*/

#include <iostream>
#include <vector>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <sstream>

std::vector<double> parseBufferToDoubles(const char* buffer) {
    std::vector<double> values;
    std::stringstream ss(buffer);
    std::string item;
    
    // Split the buffer string by commas
    while (std::getline(ss, item, ',')) {
        // Convert each part to double and add to the vector
        values.push_back(std::stod(item));
    }
    
    return values;
}

void process_command(int client_socket, InverseKinematics &ik) 
{
    char buffer[1024] = {0};
    int valread = read(client_socket, buffer, 1024);
    if (valread > 0) {
        //std::cout << "Received command: " << buffer << std::endl;

        const std::vector<double> desiredValue =  parseBufferToDoubles(buffer);

        std::vector<double> solution;
        if(!ik.solve(desiredValue, solution))
        {
            std::cerr << "ERROR: failed to find a solution!\n";
        }


        write(client_socket, solution.data(), solution.size() * sizeof(double));
    }
}

int main() 
{
    int server_fd, new_socket;
    struct sockaddr_in address;
    int addrlen = sizeof(address);

    // Creating socket file descriptor
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) 
    {
        perror("socket failed");
        exit(EXIT_FAILURE);
    }

    // Forcefully attaching socket to the port 8080
    int opt = 1;
    if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt))) 
    {
        perror("setsockopt");
        exit(EXIT_FAILURE);
    }
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(8080);

    // Forcefully attaching socket to the port 8080
    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0) 
    {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }
    if (listen(server_fd, 3) < 0) {
        perror("listen");
        exit(EXIT_FAILURE);
    }
    if ((new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t*)&addrlen)) < 0)
    {
        perror("accept");
        exit(EXIT_FAILURE);
    }

    //InverseKinematics calls keeps track of the last solution and uses it as guess for new solution.
    InverseKinematics ik;

    // Process commands until terminated
    int i=0;
    while (true) {
        process_command(new_socket, ik);
    }
    return 0;
}
