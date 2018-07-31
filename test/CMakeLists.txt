add_executable(lib_test
    main.cpp
)

target_link_libraries(lib_test lib Catch)

add_test(NAME lib_test
         COMMAND $<TARGET_FILE:lib_test>)
