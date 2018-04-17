add_executable(lib_test
    main.cpp
)

target_link_libraries(lib_test lib Catch)

add_test(NAME lib_test
         COMMAND $<TARGET_FILE:lib_test>)

find_package( PythonInterp 3.5 REQUIRED )
add_test(NAME clang_format_compliance
         COMMAND ${PYTHON_EXECUTABLE} ${CMAKE_SOURCE_DIR}/support/clang-format/run-clang-format.py --ignore external --ignore build
         WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})