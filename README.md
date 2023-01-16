# Paired-Reads-Assemble
<p>you should assemble two types of reads using the De Bruijn graph representation and the Eulerian path to obtain the original sequence from that representation.</p>
<b>Pair-reads with a known distance between them</b>

Input : Your program should be able to read a file.
The first line would be: - the length of the sequences in each side and the length of  the gap.
                         - Each read will take one.
                         - The pair reads will be separated by “|” .. Example : AGCC|TTAA
Output : The program then outputs the assembled sequence to the screen.


<h1>Explain</h1>

<b>READS</b> 
<p>GACC|GCGC</p>
<p>ACCG|CGCC</p>
<p>CCGA|GCCG</p>
<p>CGAG|CCGG</p>
<p>GAGC|CGGA</p>

<b>GRAPH</b> 
<p>(S)GAC,GCG --> ACC,CGC</p>
<p>ACC,CGC --> CCG,GCC</p>
<p>CCG,GCC --> CGA,CGC</p>
<p>CGA,CCG --> GAG,CGG</p>
<p>GAG,CGG --> AGC,GGA(E)</p>


<b>PATHS</b> 
<b>use the first letter only in all expect the last one get all its letters</b>

<p>GAC -> ACC -> CCG -> CGA -> GAG -> AGC</p>
<p>Prefix = GACCGAGC</p>

<p>GCG -> CGC -> GCC -> CCG -> CGG -> GGA</p>
<p>suffix = GCGCCGGA</p>

<h2>the final result should be like</h2>
<p>Genome = GACCGAGCGCCGGA</p>
