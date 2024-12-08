def create_codon_dict(file_path):
    path="data/codons.txt"
    file = open(path)
    rows = file.readlines()
    file.close()
    dictionary={}
    for row in rows:
        row = row.strip().split('\t')
        codon = row[0]
        amino_acid = row[2]
        dictionary[codon] = amino_acid
    return dictionary

