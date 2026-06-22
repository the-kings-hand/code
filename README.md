# The King's Hand: Thomas Cromwell and letters at the court of Henry VIII

This repository accompanies the book <i><a href="https://manchesteruniversitypress.co.uk/9781807070229/">The King's Hand: Thomas Cromwell and letters at the court of Henry VIII</a></i> (Manchester University Press, 2027) by Caitlin Burge.

![The King's Hand: Thomas Cromwell and letters at the court of Henry VIII ](KH.jpg)

Using epistolary networks built from over 30,000 letters in the State Papers of England between 1523 and 1547, The king's hand offers a new approach to the career and legacy of Thomas Cromwell, Henry VIII's right hand man and 'most faithful servant'. This book foregrounds for the first time Cromwell's use of correspondence to manage and maintain his control and authority, using digital and quantitative methodologies from historical and social network analysis to demonstrate his position in power structures at court, and offering fresh insight into his relationships with the king, other advisors at court, and the lasting impact of his administrative changes. In doing so, it uses quantitative measures to argue that Cromwell was a minister and advisor entirely unparalleled and unique in influence and power in the Henrician reign and beyond.

Each chapter utilises a separate piece of code, as listed below (note: each file name is prefaced by its respective chapter number).

<h4>Chapter 2. A rise to power: Cromwell, Wolsey, and shared epistolary networks, 1522-34</h4>
<br/>FILE(S): `cumulative_contacts.py`; `overlap_contacts.py`
<br/>The first part, <code>cumulative_contacts.py</code> , identifies Thomas Cromwell's correspondents for each year between 1522 and 1533, adding them in successive graphs to calculate number of returning or consistent contacts in cumulative years.

The second part, <code>overlap_contacts.py</code> , identifies both Thomas Cromwell and Thomas Wolsey's correspondents for each year between 1522 and 1533, adding them in successive graphs to calculate the number of shared contacts over cumulative years. This also creates a Gephi file for each cumulative graph.

<b>Chapter 3. King and minister: Modelling data and power dynamics</b>
<br/>FILE(S): `king_references.py`
<br/>       This file establishes

<b>Chapter 4. The court lynchpin: Cromwell and network functionality</b>
<br/>FILE(S): `removal_model.py`

<b>Chapter 5. The King's gatekeeper: Intermediaries in the network</b>
<br/>FILE(S): `gatekeeper_triads.py` (written in collaboration with Dr Sebastian Ahnert, University of Cambridge)

<b>Chapter 7. Cromwell's legacy: Administrative structures in the network</b>
<br/>FILE(S): `model_comparison.py`

<i>All code here requires NetworkX and has been tested on Python 3.9.6. The current working directory needs to be set as the-kings-hand/code for code and file imports to operate correctly.</i>