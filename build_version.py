# This Python file uses the following encoding: utf-8

import os

def read_build_version():
    # open input file
    file_name = "./pycrypto.pyproject.user"
    if (not os.path.isfile(file_name)):
        return "(error opening version file)"
    file_input = open(file_name, "rb")
    file_data = file_input.readlines()
    file_input.close
    data = str(file_data[2])
    start = data.find(",")
    build_date = data[start+2:]
    end = build_date.find(".")
    build_date = build_date[:end].replace("-", "").replace(":", "").replace("T", ".")
    return build_date
