#!/usr/bin/env python

#
# Generate (optionally) unique random names with real world probability weighting of first / last name
#
# NB, names are not guaranteed to be unique across male and female generations.
#
# Data Obtained from http://www.census.gov/genealogy/www/data/1990surnames/names_files.html
#
# Data files used:
#     data/dist.all.last
#     data/dist.female.first
#     data/dist.male.first
#
# Andrew Cutler 2012-04-07
#

import os
import sys
from random import shuffle
from optparse import OptionParser
import json

from name_generator import parse_data, generate_names
from name_generator.wc import WeightedChoice
from name_generator.settings import DATA_PATH


def main():
    parser = OptionParser()
    parser.add_option("-u", "--unique", action="store_true", dest="unique", default=False,
                      help="Generate unique names (within a given sex)")
    parser.add_option("-m", "--male", action="store", type="int", dest="num_male", default=0,
                      help="Number of male names")
    parser.add_option("-f", "--female", action="store", type="int", dest="num_fem", default=0,
                      help="Number of female names")
    (options, args) = parser.parse_args()

    if len(sys.argv) == 1:
        parser.error("No arguments")
    elif len(args) != 0:
        parser.error("Wrong number of arguments")
    else:
        # Parse data
        # file_path = lambda x: os.path.join(os.path.split(__file__)[0], '..', 'data', x)
        file_path = lambda x: os.path.join(DATA_PATH, x)
        fem_data = parse_data(file_path('dist.female.first'))
        male_data = parse_data(file_path('dist.male.first'))
        last_data = parse_data(file_path('dist.all.last'))

        # Create Objects
        fem_wc = WeightedChoice(fem_data);
        male_wc = WeightedChoice(male_data);
        last_wc = WeightedChoice(last_data);

        i = 3
        j = 3
        flag = 0

        output_male_wash = []
        output_fem_wash = []
        # Generate Female Names

        if options.num_fem > 0:
            output_fem = generate_names(fem_wc, last_wc, options.num_fem, options.unique)
            shuffle(output_fem)
            output_fem_wash = list(set(output_fem))
            print('female:' + str(len(output_fem_wash)))


        # Generate Male Names
        if options.num_male > 0:
            output_male = generate_names(male_wc, last_wc, options.num_male, options.unique)
            shuffle(output_male)
            output_male_wash = list(set(output_male))
            print('male:' + str(len(output_male_wash)))

        # Randomly shuffle the output so male and female names are mixed


        dic = {}
        dic['male_name'] = []
        dic['female_name'] = []
        for name in output_fem_wash:
            dic['female_name'].append(name)
        for name in output_male_wash:
            dic['male_name'].append(name)
        json_data = json.dumps(dic)
        f = open('name_text.json', 'w')
        f.write(json_data)
        f.close()


if __name__ == '__main__':
    main()
