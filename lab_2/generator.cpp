#include <iostream>
#include <ctime>

using namespace std;

void generating_binary_sequence(int n) {
 /**
 * Function initializes the random number generator using the current time and generates
 * n-bit binary sequence, printing it to the standard output.
 * @param n - number of bits in sequence
 * @return None
 */
    srand(static_cast<unsigned>(time(0)));

    for (int i = 0; i < n; ++i) {
        int bit = rand() % 2;
        cout << bit;
    }
}


int main() {
 /**
 * The main function calls generating_binary_sequence to generate a random binary sequence
 * and print it to the standard output.
 * @return The program exit code.
 */
    int n;
    cout << "Enter number of bits for sequence: "; // we need use 128-bit sequence
    cin >> n;
    generate_binary_sequence(n);
    return 0;
}