cmake_minimum_required(VERSION 3.25)
project(cpp_study)

set(CMAKE_CXX_STANDARD 11)

add_executable(cpp_study main.cpp)
add_executable(base_syntax.input_data base_syntax/input_data.cpp)
add_executable(base_syntax.condition base_syntax/condition.cpp)