FROM python:3.5-slim

RUN mkdir repo
ADD . /repo

CMD ["python", "repo/support/clang-format/run-clang-format.py"]
