def to_rna(DNA):
	RNA = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
	return ''.join([RNA[x] for x in DNA])