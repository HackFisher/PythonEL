# Random Male and Female name generator

Generates random male and female names with real-world probability. (Well the occurrence of first name and last names, not the combination of the two).

## Install

Dev:

    pip install -e git+https://github.com/macropin/random-name-generator.git#egg=name_generator

Prod:

    pip install git+https://github.com/macropin/random-name-generator.git

## Usage Examples
    产生10个不同的male姓名以json格式存入name_text.json中
    ./name_generator.py -u -m 10
    产生10个允许相同的male和female姓名以json格式存入name_text.json中
    ./name_generator.py -m 5 -f 5

    name_text.json
    {"female_name": ["LATASHA ROSARIO", "JENNA BLACKBURN", "LENORE BYRD", "CHRISTINA HATTAWAY", "LAURA LUCAS"], "male_name": ["CLARENCE FORD", "RONALD DODGEN", "RANDY ARROWOOD", "JARED LACY", "EVAN GARY"]}

