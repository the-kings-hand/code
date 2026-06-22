<h2>The King's Hand - Correspondence Network Data</h2>

The dataset here is a subset of the Tudor Networks of Power Correspondence Dataset by Ruth Ahnert, Sebastian Ahnert, Jose Crese, and Lotte Fickers. Full details of the original dataset, including Creative Commons Licence and dataset creation description, can be found at the <a href="https://github.com/tudor-networks-of-power/code/tree/main/TNP_DATA">Tudor Networks of Power Github Repository</a>. 

These data consist of a directed edgelist (writer, recipient) of all known letters contained in _Letters and Papers, Foreign and Domestic, Henry VIII_ from 1522 to 1547, covering Thomas Cromwell's period in the State Papers through to the end of Henry VIII's reign. These use unique identifiers to refer to indivdual writers in the correspondence, applied as part of an extensive disambiguation and dedupliation process undertaken by Ahnert and Ahnert (see <a href="https://global.oup.com/academic/product/tudor-networks-of-power-9780198858973?cc=gb&lang=en&#"><i>Tudor Networks of Power</i></a>).

This dataset contains:
<ul>
<li><code>1534-1540.csv</code> - directed edgelist of letters covering Thomas Cromwell's service under Henry VIII, containing just writer and recipient (for Chapters 2 - 4)</li>
<li><code>Jan-July 1540.csv</code> - directed edgelist of letters covering Thomas Cromwell's last six months in power, containing just writer and recipient (for Chapter 5)</li>
<li><code>1540-1547.csv</code> - directed edgelist of letters covering the last years of Henry VIII's reign after the death of Thomas Cromwell, containing just writer and recipient (for Chapter 7)</li>
<li><code>all_letters.csv</code> - directed edgelist of all letters used throughout, containing just writer and recipient</li>
<li><code>full_person_list.csv</code> - Key for the person IDs used (from <a href="https://github.com/tudor-networks-of-power/code/tree/main/TNP_DATA">Tudor Networks of Power Correspondence Dataset</a>)</li>
<li><code>Years [folder]</code> - individual csvs of letters in each year in the dataset, necessary for some code</li>
</ul>
If using this dataset and associated code, please cite:

Caitlin Burge, "The King's Hand: Thomas Cromwell and Letters at the court of Henry VIII", Manchester University Press, 2027.

R. Ahnert, S E. Ahnert, "Tudor Networks of Power", Oxford University Press, 2023.

R. Ahnert, S. E. Ahnert, J. Cree, & L. Fikkers, "Tudor Networks of Power - correspondence network dataset". Apollo - University of Cambridge Repository (2023). https://doi.org/10.17863/CAM.99562
