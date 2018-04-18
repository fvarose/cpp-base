import argparse
import logging
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
    logging.info('Ignoring the following paths: %s', ignored_paths)
    cpp_files = []
    for path, dirs, files in os.walk('./'):
        if len([p for p in ignored_paths if '/{}'.format(p) in path]) > 0:
            continue
        for file in files:
            if file.endswith(".cpp"):
                cpp_files.append(os.path.join(path, file))
    logging.info('Found %i C++ files to check', len(cpp_files))
    return cpp_files

def _is_clang_formatted(filepath):
    clang_format_args = ['clang-format', '-output-replacements-xml', '-style=file', filepath]
    try:
        xml_output = subprocess.check_output(clang_format_args)
    except:
        logging.error('Could not run the following command: `%s`', ' '.join(clang_format_args))
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
        logging.error('Found some files that are not formatted with clang-format: %s', bad_files)
        exit(1)
    exit(0)

if __name__ == "__main__":
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO, stream=sys.stdout)
    main()