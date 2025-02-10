def get_gene(data_file):
    Dm_Ds = []
    with open(data_file, 'r') as file:
        for line in file:
            parts = line.strip().split(",") 
            if parts[0] in ["Drosophila melanogaster", "Drosophila simulans"]:
                Dm_Ds.append(parts[2])
    return Dm_Ds

def gene_exp(data_file):
    results = {}
    with open(data_file, 'r') as file:
        for line in file:
            parts = line.strip().split(",")
            gene_sequence = parts[1] 
            gene_name = parts[2] 
            
            at_content = (gene_sequence.count('A') + gene_sequence.count('T')) / len(gene_sequence)

            if at_content > 0.65:
                category = "high"
            elif at_content < 0.45:
                category = "low"
            else:
                category = "medium"

            results[gene_name] = category 
            print(f"Gene {gene_name} has {category} AT content.")
    return results

def test_gene_exp():
    data_file = "gene_data.csv"
    results = gene_exp(data_file)
    assert results["kdy647"] == "high AT content"
    assert results["jdg766"] == "medium AT content"
    print("All tests passed!")
test_gene_exp()
