import random

attribute_20bit_name = ['appearance', 'pattern', 'eye_color', 'eye_shape', 'main_color', 'pattern_color',
                        'dotted_color', 'mouth', 'mouth_color', 'environment', 'secret', 'time_attribute']

double_random = [[2*x,2*x+1] for x in range(0,8)]

'''
返回gene列表为gene序列转化为十进制数值列表
'''


def generate_gene_double_time(num):
    gene_list = []
    for i in range(num):
        flag = []
        flag.append(random.randint(0, 1))
        flag.append(abs(flag[0] - 1))
        attribute_index = random.randint(0, 7)
        gene_double = []
        for j in range(2):
            gene = 0b1
            race = 1
            sex = j
            reproductive = 1
            attribute_20bit = {}

            for attribute in attribute_20bit_name:
                attribute_20bit[attribute] = [random.randint(0, 15), random.randint(0, 15), random.randint(0, 15),
                                              random.randint(0, 15)]
            attribute_20bit['time_attribute'] = [random.randint(0, 15), random.randint(0, 15), random.randint(0, 15),
                                                 double_random[attribute_index][flag[j]]]
            # print(attribute_20bit)

            gene = gene << 2
            gene += race
            gene = gene << 1
            gene += sex
            gene = gene << 1
            gene += reproductive

            for attribute in attribute_20bit:
                for num in attribute_20bit[attribute]:
                    gene = gene << 5
                    gene += num
            gene = bin(gene)[3:]
            # print(len(gene))
            gene_double.append(int(gene, 2))
        gene_list.append(gene_double)

    return gene_list


if __name__ == '__main__':
    #print(generate_gene_double_time(10))
    pass
