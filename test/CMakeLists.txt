add_executable(app_test
    main.cpp
)

add_test(NAME app_test
         COMMAND $<TARGET_FILE:app_test>)
