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


'''
返回字典对应key意义
'race':种族，目前默认为01           'sex':性别
'reproductive':繁殖能力             'appearance':外形
'pattern':花纹                     'eye_color':眼睛颜色
'eye_shape':眼睛形状                'main_color':主色                     
'pattern_color':花纹颜色            'dotted_color':点缀色              
'mouth':嘴巴                      'mouth_color':嘴巴颜色
'environment':环境                'secret':秘密
'time_attribute':限时属性
'''


def analyse_gene(gene):
    gene_dict = {}
    gene = bin(gene)[2:]
    while len(gene) != 244:
        gene = '0' + gene
    gene_dict['race'] = int(gene[0:2], 2)
    gene_dict['sex'] = int(gene[2:3], 2)
    gene_dict['reproductive'] = int(gene[3:4], 2)
    i = 19
    for attribute_name in attribute_20bit_name:
        gene_dict[attribute_name] = int(gene[i:i + 5], 2)
        i += 20
    return gene_dict


gene_list = generate_gene(100)
print(gene_list)
gene_json_list = []
for g in gene_list:
    gene_dict = analyse_gene(g)
    gene_json_list.append(gene_dict)
    print(gene_dict)
