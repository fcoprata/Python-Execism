def proteins(strand):
    """
    Translates a given RNA strand into a list of proteins.

    Args:
        strand (str): The RNA strand to be translated.

    Returns:
        list: A list of proteins translated from the RNA strand.

    Raises:
        None

    Examples:
        >>> proteins("AUGUUUUCU")
        ['Methionine', 'Phenylalanine', 'Serine']
    """
    strand = strand.upper()
    list_codons = [strand[i: i + 3] for i in range(0, len(strand), 3)]
    list_proteins = []
    for protein in list_codons:
        if protein == "UAA" or protein == "UAG" or protein == "UGA":
            break
        if protein == "AUG":
            list_proteins.append("Methionine")
        if protein == "UUU" or protein == "UUC":
            list_proteins.append("Phenylalanine")
        if protein == "UUA" or protein == "UUG":
            list_proteins.append("Leucine")
        if protein == "UCU" or protein == "UCC" or protein == "UCA" or protein == "UCG":
            list_proteins.append("Serine")
        if protein == "UAU" or protein == "UAC":
            list_proteins.append("Tyrosine")
        if protein == "UGU" or protein == "UGC":
            list_proteins.append("Cysteine")
        if protein == "UGG":
            list_proteins.append("Tryptophan")

    return list_proteins
