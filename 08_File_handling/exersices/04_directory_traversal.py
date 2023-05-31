import os
import collections


def traverse_directory(path):
    # Initialize a default dictionary with a list as the default value type
    files_by_extension = collections.defaultdict(list)

    for entry in os.scandir(path):
        if entry.is_file():
            filename, file_extension = os.path.splitext(entry.name)
            # strip the leading '.' from the extension and convert to lower case
            file_extension = file_extension[1:].lower()
            files_by_extension[file_extension].append(filename)

    # sort extensions and filenames
    for file_extension in files_by_extension:
        files_by_extension[file_extension].sort()
    sorted_extensions = collections.OrderedDict(sorted(files_by_extension.items()))

    return sorted_extensions


def write_report(path, files_by_extension):
    report_path = os.path.join(path, "report.txt")
    with open(report_path, 'w') as report:
        for file_extension, filenames in files_by_extension.items():
            report.write(f'.{file_extension}\n')
            for filename in filenames:
                report.write(f'- - - {filename}.{file_extension}\n')


path_to_directory = 'parth to the directory'
files_by_extension = traverse_directory(path_to_directory)
write_report(path_to_directory, files_by_extension)
