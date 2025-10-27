// g++ -std=c++20 ex-cpp-10.cpp -o build/ex-cpp-10 && ./build/ex-cpp-10
// -----task-source:-ai-generated------
// Zadanie 10: Konwersja temperatur
// Napisz program, który wczytuje temperaturę w stopniach Celsjusza i przelicza
// ją na stopnie Fahrenheita. Wzór: F = C * 9/5 + 32.
#include <iostream>

int main() {
  int celcius;
  int farenheit;
  std::cout << "Give me temperature in Celcius and I'll calculate "
               "Fahrenheit.\n";
  std::cin >> celcius;
  farenheit = celcius * 9 / 5 + 32;
  std::cout << "Here is your temperature in Fahrenheit: " << farenheit
            << std::endl;
  return 0;
}
// ----------- Future Tips: -----------
