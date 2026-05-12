# HK_PhD_general
Single use (non-pipeline) scripts involved in HK PhD project.
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
## Cosinor_model_fitting.py

Fits a cosnor model to single gene expression data sampled across a 24-hour period. Will accept multiple `tsv` files, generate per gene summary statistics (MESOR, Amplitude + SE, Acrophase radians, Acrophase hours, R2 and ZeroAMp pvalue) and publication quality `PDF` figures with each figure scaled to the same axis scales.

**Input data requirements:**

Column headers should be as follows:

| mean | sd | cv | mean hk | sd hk | cv hk | ZT | expression ration (goi/hk) |
| --- | --- | --- | --- | --- | --- | --- | --- |


**User editable settings:**


```python
folder = ""                   # folder with gene .tsv files
show_points = True            # show raw data
period = 24                   # circadian period
save_summary = True           # save cosinor summary CSV
save_figures = True           # export each plot as PDF
```

---
