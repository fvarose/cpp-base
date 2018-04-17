import argparse
import os
import sys

def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ignore', action='append', dest='ignore',
                        default=[],
                        help='Paths that should be ignored when looking for C++ files',
                       )
    return parser.parse_args()

def _find_cpp_files(ignored_paths):
    print('Info: ignoring the following paths:', ignored_paths)
    cpp_files = []
    for dirpath, dnames, fnames in os.walk('./'):
        if len([p for p in ignored_paths if '/{}/'.format(p) in dirpath]) > 0:
            continue
        for f in fnames:
            if f.endswith(".cpp"):
                cpp_files.append(os.path.join(dirpath, f))
    return cpp_files

def _is_clang_formatted(file):
    return False

def main():
    args = _parse_args()

    cpp_files = _find_cpp_files(args.ignore)

    bad_files = [f for f in cpp_files if not _is_clang_formatted(f)]

    if len(bad_files) > 0:
        print('Error: found some files that are not formatted with clang-format:', bad_files)
        exit(1)
    exit(0)

if __name__ == "__main__":
    main()