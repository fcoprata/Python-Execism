def to_rna(dna_strand):
    """
    Transcribes a DNA strand into its RNA complement.

    Args:
        dna_strand (str): The DNA strand to be transcribed.

    Returns:
        str: The RNA complement of the given DNA strand.

    Raises:
        ValueError: If an invalid nucleotide is encountered in the DNA strand.

    Examples:
        >>> to_rna("GCTA")
        'CGAU'
        >>> to_rna("ACGT")
        'UGCA'

    The function `to_rna` takes a DNA strand as input and returns its RNA complement. It converts each nucleotide in the DNA strand to its corresponding nucleotide in RNA. The valid nucleotides are 'G', 'C', 'T', and 'A'. If an invalid nucleotide is encountered, a `ValueError` is raised.

    Example usage:
    ```python
    >>> to_rna("GCTA")
    'CGAU'
    >>> to_rna("ACGT")
    'UGCA'
    ```
    """
    dna_strand = dna_strand.upper()
    rna_strand = ""
    for nucleotide in dna_strand:
        if nucleotide == "G":
            rna_strand += "C"
        elif nucleotide == "C":
            rna_strand += "G"
        elif nucleotide == "T":
            rna_strand += "A"
        elif nucleotide == "A":
            rna_strand += "U"
        else:
            raise ValueError("Invalid nucleotide")
    return rna_strand
