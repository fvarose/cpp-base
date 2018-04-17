import argparse
import os
import subprocess
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
    for path, dirs, files in os.walk('./'):
        if len([p for p in ignored_paths if '/{}'.format(p) in path]) > 0:
            continue
        for file in files:
            if file.endswith(".cpp"):
                cpp_files.append(os.path.join(path, file))
    print('Info: found {} C++ files to check'.format(len(cpp_files)))
    return cpp_files

def _is_clang_formatted(filepath):
    clang_format_args = ['clang-format', '-output-replacements-xml', '-style=file', filepath]
    try:
        xml_output = subprocess.check_output(clang_format_args)
    except:
        print('Error: could not run the following command: `{}`'.format(' '.join(clang_format_args)))
        exit(2)
        
    for line in xml_output.splitlines():
        if line.startswith(b'<replacement '):
            return False
    return True

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