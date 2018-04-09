[![Build Status](https://travis-ci.org/fvarose/cpp-base.svg?branch=master)](https://travis-ci.org/fvarose/cpp-base)
[![Build status](https://ci.appveyor.com/api/projects/status/vl7sfpx2s8bw38ab/branch/master?svg=true)](https://ci.appveyor.com/project/fvarose/cpp-base/branch/master)

# cpp-base
Base repo setup for a C++ project.

## Features
- C++17 enabled
- All warnings turned on and treated as errors
- [Catch2](https://github.com/catchorg/Catch2/) for unit tests
- Builds on Travis for the following configs:
  - OSX / apple-clang-9.0.0
  - Ubuntu (Trusty) / g++-6

## Building

    cd cpp-base
    mkdir build && cd build
    cmake .. && cmake --build .

## Run tests

    cd cpp-base/build
    ctest
