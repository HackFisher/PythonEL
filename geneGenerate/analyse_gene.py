attribute_20bit_name = ['appearance', 'pattern', 'eye_color', 'eye_shape', 'main_color', 'pattern_color',
                        'dotted_color', 'mouth', 'mouth_color', 'environment', 'secret', 'time_attribute']

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


if __name__ == '__main__':
    pass
