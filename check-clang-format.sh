#!/bin/sh
docker build -t support/clang-format -f ./support/clang-format/Dockerfile .
docker run support/clang-format
