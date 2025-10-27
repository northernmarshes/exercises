// g++ -std=c++20 ex-cpp-04.cpp -o build/ex-cpp-04 && ./build/ex-cpp-04
// -----task-source:-ai-generated------
// Zadanie 4: Wczytywanie imienia
// Napisz program, który pyta użytkownika o imię, a następnie wyświetla
// powitanie z tym imieniem.
#include <iostream>
#include <string>

int main() {
  std::string name;
  std::cout << "What is your name?\n";
  std::cin >> name;
  std::cout << "Hello, " << name << "! Nice to meet you :)" << std::endl;
  return 0;
}

// ----------- Future Tips: -----------
// Returning here after python feels like
// driving a 100 years old heavy tank
