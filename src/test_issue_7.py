#NOTE: I included this file here, only for test purpose.
# I may lack proper testing knowledge :)

import os
from guerilla_parser.parser import GuerillaParser

filepath =os.path.abspath(
    os.path.join(os.getcwd(), r"..\test\gproject\2.4.3\environment_mode_type.gproject")
)

parser = GuerillaParser.from_file(filepath)

