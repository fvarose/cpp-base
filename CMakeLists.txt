project(app)

cmake_minimum_required(VERSION 3.9)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

include(cmake/warnings.cmake)

add_subdirectory(app)
add_subdirectory(lib)

enable_testing()
add_subdirectory(external/Catch2)
add_subdirectory(support/clang-format)
add_subdirectory(test)