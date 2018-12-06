from generate_gene import generate_gene
from analyse_gene import analyse_gene
from generate_gene_double_time import generate_gene_double_time

gene_list = generate_gene_double_time(100)

gene_list = generate_gene(20)

print(gene_list)
gene_json_list = []
for item in gene_list:
    # for item in g:
    gene_dict = analyse_gene(item)
    gene_json_list.append(gene_dict)
    print(gene_dict)
    print('')
