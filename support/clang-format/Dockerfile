FROM python:3.5-slim

RUN mkdir repo
ADD . /repo
WORKDIR repo

CMD ["python", "support/clang-format/run-clang-format.py"]
