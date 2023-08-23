# This Python file uses the following encoding: utf-8

import os

def read_build_version():
    # open input file
    file_name = "./build_number"
    if (not os.path.isfile(file_name)):
        return "0000.0"
    file_input = open(file_name, "rb")
    file_data = file_input.readlines()
    file_input.close
    build_date = file_data[0].decode("utf-8").replace("\n", "") + "." + file_data[1].decode("utf-8").replace("\n", "")
    return build_date
