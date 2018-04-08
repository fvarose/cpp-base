add_executable(app_test
    main.cpp
)

target_link_libraries(app_test lib Catch)

add_test(NAME app_test
         COMMAND $<TARGET_FILE:app_test>)
