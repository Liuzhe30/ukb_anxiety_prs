# ukb_anxiety_prs

## GWAS of the Gut microbiota and anxiety
The Gut microbiota cohort used in this study was released by [E. A. Lopera-Maya, et al.](https://www.nature.com/articles/s41588-021-00992-y) and the anxiety cohort was selected from the [UK biobank](https://www.ukbiobank.ac.uk/).

## Regenie cmds
We use [Regenie](https://github.com/rgcgithub/regenie) to generate GWAS files of anxiety paticipants of UKB, and we provide the [phenotype file](https://github.com/Liuzhe30/ukb_anxiety_prs/tree/main/case-control/datafile/ukb_phenotypes_BT.txt) and the [covariate file](https://github.com/Liuzhe30/ukb_anxiety_prs/tree/main/case-control/datafile/ukb_covariates.txt).
The cmds used are as follows:
```

```

## PRSice cmds
We use [PRSice-2](https://github.com/choishingwan/PRSice) to generate PRS scores. The cmds used are as follows:
```
Rscript PRSice.R --dir . \
    --prsice bin/PRSice \
    --extract PRSice.valid \
    --out UKB-DMP447  \
    --base ../../ukbiobank/DMPcohort_BetaOR/GCST90027447_buildGRCh37.tsv \
    --thread 1 \
    --stat beta \
    --binary-target T \
    --target ../UKBsample/chr#,../UKBsample/ukb_cal_allChrs.fam \
    --chr chromosome \
    --snp variant_id \
    --bp base_pair_location --A1 effect_allele --A2 other_allele --pvalue p_value \
    --pheno ../UKBsample/ukb_phenotypes.txt \
    --cov ../UKBsample/ukb_covariates.txt
```

## MR cmds
We use [TwoSampleMR](https://mrcieu.github.io/TwoSampleMR/) to perform the Mendelian randomization analysis. The cmds used are as follows:
```

```