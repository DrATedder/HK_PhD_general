# HK_PhD_general
Single use scripts involved in HK PhD project.
---

## HK_cage_randomisation.py

Generates a semi-random sampling schedule with the following rules:
- 48 individuals comprising 24 males and 24 females.
- Individuals are housed in single sex enclosures 4 individuals per enclosure.
- Individuals are sampled at 6 equal time points between 0 and 24 hours (0, 4, 8, 12, 16, 20).
- At each time point 4 male individuals and four female individuals must be sampled.
- No Individual can be left in it's enclosure on it's own at any point.
- No single enclosure can be completely sampled at any single timepoint (max 2 individuals per enclosure per timepoint)
- Individuals are named in the following way: sex-number-enclosure; where sex= male or female, number is between 1-24 and enclosure is between 1-12.

**Specifics:**
- Includes random seed.
- Sampling balances enclosure selection across timepoints with maximum temporal dispertion.

**Output:**
- Text of sampling strategy.
- Visualisation of enclosure clustering.

---
