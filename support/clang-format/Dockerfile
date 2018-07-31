FROM ubuntu:xenial

# Install `wget` and `apt-add-repository`
RUN apt-get update
RUN apt-get install -y wget
RUN apt-get install -y software-properties-common

# Install clang-format
RUN wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add -
RUN apt-add-repository "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial main"
RUN apt-get update
RUN apt-get install -y clang-format-7

RUN ln -s /usr/bin/clang-format-7 /usr/bin/clang-format

# Run script
RUN mkdir repo
ADD . /repo
WORKDIR repo

CMD ["python", "support/clang-format/check-clang-format.py",\
    "--ignore=external"]
