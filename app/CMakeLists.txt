add_executable(app
    main.cpp
)

max_warnings_level(app)
treat_warnings_as_errors(app)

target_link_libraries(app lib)
