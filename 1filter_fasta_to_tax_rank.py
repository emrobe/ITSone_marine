import HTSeq, argparse

parser = argparse.ArgumentParser(description="This script filters out any fasta sequences (child node) NOT part of the NCBI taxonomy hierarchy under a given taxonomic rank (parent node). Fasta sequences need to have NCBI tax id in column 3 in the fasta header (separated by '|'). \nThis is script is tailored to use ITSone fasta formatted headers")
parser.add_argument('--fasta', help="Fasta file to be filtered.", type=str)
parser.add_argument('--taxidlinage', help="Path to the taxidlinage.dmp file obtainable from NCBI taxonomy ftp.", type=str)
parser.add_argument('--rank', help="Parent node (Defaults to Fungi, 4751)", type=int, default=4751)
args = parser.parse_args()

nodes = []
nodes.append(args.rank)

# Map taxonomic ranks to top level (args.rank)
with open (args.taxidlinage) as taxset:
    for line in taxset:
        linelist = line.split("|")
        linelist = [tax.strip() for tax in linelist]
        
        # Some ranks such as 1 and 131567 no not have parent nodes and are irrelevant
        if not linelist[1]:
            continue

        rank, parents = int(linelist[0].strip()), linelist[1].split()
        
        # Make sure all taxid are ints
        parents = list(map(int, parents))

        if args.rank in parents:
            nodes.append(rank)

# Tax-check and write fasta sequences 
for seq in HTSeq.FastaReader(args.fasta, raw_iterator=True):
    # Header with no greater than sign
    header = ' '.join(list(seq[1:]))
    # int of taxid
    tax = header.split("|")
    tax = int(tax[2])
    # Complete header
    fastaheader = '>'+header
    
    if tax in nodes:
        print fastaheader
        print seq[0]
