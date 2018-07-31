[![Build Status](https://travis-ci.org/fvarose/cpp-base.svg?branch=master)](https://travis-ci.org/fvarose/cpp-base)
[![Build status](https://ci.appveyor.com/api/projects/status/vl7sfpx2s8bw38ab/branch/master?svg=true)](https://ci.appveyor.com/project/fvarose/cpp-base/branch/master)

# cpp-base
Base repo setup for a C++ project.

## Features
- C++17 enabled
- All warnings turned on and treated as errors
- [Catch2](https://github.com/catchorg/Catch2/) for unit tests
- CI integration for the following configs:
  - Travis CI
    - OSX / apple-clang-9.0.0
    - Ubuntu (Trusty) / g++-6
  - AppVeyor
    - Windows / Visual Studio 15 2017
- Code formatting checked automatically with `clang-format-7`:
  - locally: trigerred as a separate test (requires Docker)
  - CI: "format" stage defined in Travis CI

## Building locally

    cd cpp-base
    mkdir build && cd build
    # OSX / Linux
    cmake .. && cmake --build .
    # Windows
    cmake .. && cmake --build . --config Release

## Run tests

    cd cpp-base/build
    ctest
