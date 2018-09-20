# ITSone fungi marine non-redundant

ITSone marine sequences subset provided by IBIOM is refined using the World Register of Marine Species (WoRMS) API using AphiaIDByName and only_marine=True. The subset is obtainable via http://itsonedb.cloud.ba.infn.it/ITS1Marine/

### ELIXIR Norway procurement workflow:
1. Sequences are filtered to the Fungi (NCBI taxid: 4751) top rank using the script '1filter_fasta_to_tax_rank.py'. The script requires the taxidlineage.dmp file from the NCBI Taxonomy FTP (part of the new_taxdump.tar.gz tax-dump as of 2018) 
2. Sequences are filtered for duplication. HMM annotations are preferred over ENA annotations.

The final dataset "ITSone_fungi_marine_nr.fasta" consists of 12341 sequences (marine, fungi, non-redundant).
