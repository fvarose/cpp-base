#!/usr/bin/python3
# -*- coding: utf-8-*-
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
            if file.endswith('.cpp') or file.endswith('hpp') or file.endswith('.h'):
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

    logging.info('Using clang-format version:\n%s', subprocess.check_output(['clang-format', '--version']))

    cpp_files = _find_cpp_files(args.ignore)

    bad_files = [f for f in cpp_files if not _is_clang_formatted(f)]

    if len(bad_files) > 0:
        logging.error('Found %i files that are not formatted with clang-format:', len(bad_files))
        for file in bad_files:
            logging.error('- %s', file)
        exit(1)
    logging.info('Success: all %i files are correctly formatted 😌', len(cpp_files))
    exit(0)

if __name__ == "__main__":
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO, stream=sys.stdout)
    main()