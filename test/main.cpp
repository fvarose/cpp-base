#define CATCH_CONFIG_MAIN // This tells Catch to provide a main() - only do this
                          // in one cpp file
#include <catch.hpp>

#include <dummy.hpp>

TEST_CASE("A dummy test case") {
  dummy d{};
  CHECK(is_dummy(d) == false);
}