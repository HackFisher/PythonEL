# geneGenerate

## generate_gene.py
包含函数generate_gene（num），作用为随机产生num个基因序列

输入：产生所需基因序列的数量num

输出：包含num个的随机二进制基因序列转换为10进制的整数list

| 种族 | 性别 | 繁殖 | 其他*12 |
| - | :-: | -: | -: |
| 2bit | 1bit | 1bit | 12*20bit |


产生基因序列为244位

#### 按照规则产生所需基因数据：

- 默认种族为1（0b01）

- 性别、繁殖为0-1随机数

- 其余20bit属性每个均由R3（5bit），R2（5bit），R1（5bit），D0（5bit）组成

    - R3，R2，R1，D0为0-15随机数



## analyse_gene.py
包含函数analyse，作用为解析10进制基因数值

输入：基因序列转换为10进制的整数

输出：包含显性基因和其他基因属性的字典值


## gene_collection.py
包含以上所有文件的代码

## generate_gene_double.py
生成基于限时属性的成对基因组

种族：1

性别：0 and 1

繁殖能力：1

appearance～secret：[0-15]随机数

time_attribute:[[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15]]基因对

## main.py
主函数，为调用以上函数的测试样例
