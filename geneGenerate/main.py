from generate_gene import generate_gene
from analyse_gene import analyse_gene

gene_list = generate_gene(100)
print(gene_list)
gene_json_list = []
for g in gene_list:
    gene_dict = analyse_gene(g)
    gene_json_list.append(gene_dict)
    print(gene_dict)
