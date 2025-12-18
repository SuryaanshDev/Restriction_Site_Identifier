def find_restriction_sites(dna_sequence, enzymes):

    dna_sequence = dna_sequence.upper()
    results = {}

    for enzyme, site in enzymes.items():

        positions = []
        site_length = len(site)

        for i in range(len(dna_sequence) - site_length + 1):
            if dna_sequence[i:i + site_length] == site:
                positions.append(i + 1)

        if positions:
            results[enzyme] = {
                "recognition_site": site,
                "positions": positions
            }

    return results 


dna = input("Enter a DNA Sequence: ").strip()

restriction_enzymes = {
    "EcoRI": "GAATTC",
    "BamHI": "GGATCC",
    "HindIII": "AAGCTT",
    "NotI": "GCGGCCGC",
    "AluI": "AGCT"
}

results = find_restriction_sites(dna, restriction_enzymes)

if results:
    print("\nRestriction sites found:\n")

    for enzyme, info in results.items():
        print(enzyme)
        print(f"  Site: {info['recognition_site']}")
        print(f"  Positions: {info['positions']}")
else:
    print("No restriction sites found.")
