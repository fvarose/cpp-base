add_library(lib
    dummy.hpp
    dummy.cpp
)

max_warnings_level(lib)
treat_warnings_as_errors(lib)

target_include_directories(lib PUBLIC .)
