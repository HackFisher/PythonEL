import random

attribute_20bit_name = ['appearance', 'pattern', 'eye_color', 'eye_shape', 'main_color', 'pattern_color',
                        'dotted_color', 'mouth', 'mouth_color', 'environment', 'secret', 'time_attribute']

'''
返回gene列表为gene序列转化为十进制数值列表
'''


def generate_gene(num):
    gene_list = []
    for i in range(num):
        gene = 0b1
        race = 1
        sex = random.randint(0, 1)
        reproductive = random.randint(0, 1)
        attribute_20bit = {}

        for attribute in attribute_20bit_name:
            attribute_20bit[attribute] = [random.randint(0, 15), random.randint(0, 15), random.randint(0, 15),
                                          random.randint(0, 15)]
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
        # print(gene)
        # print(len(gene))
        gene_list.append(int(gene, 2))
    return gene_list


if __name__ == '__main__':
    pass
