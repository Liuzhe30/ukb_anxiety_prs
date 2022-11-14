# ukb_anxiety_prs

## GWAS of the Gut microbiota and anxiety
The Gut microbiota cohort used in this study was released by [E. A. Lopera-Maya, et al.](https://www.nature.com/articles/s41588-021-00992-y) and the anxiety cohort was selected from the [UK biobank](https://www.ukbiobank.ac.uk/).
Since the size of our [PRS score dataset](https://github.com/Liuzhe30/ukb_anxiety_prs/tree/main/case-control/datafile/PRS_dataset.pkl) is larger than 1G, please us "git-lfs" to clone our repo:
```
git-lfs clone https://github.com/Liuzhe30/ukb_anxiety_prs
```

## Regenie cmds
We use [Regenie](https://github.com/rgcgithub/regenie) to generate GWAS files of anxiety paticipants of UKB, and we provide the [phenotype file](https://github.com/Liuzhe30/ukb_anxiety_prs/tree/main/case-control/datafile/ukb_phenotypes_BT.txt) and the [covariate file](https://github.com/Liuzhe30/ukb_anxiety_prs/tree/main/case-control/datafile/ukb_covariates.txt).
The cmds used are as follows:
```
./plink \
  --bed ukb22418_c1_b0_v2.bed \
  --bim ukb_snp_chr1_v2.bim \
  --fam ukb22418_c1_b0_v2_s488170.fam \
  --merge-list merge_list_lz.txt \
  --make-bed --out ukb_cal_allChrs
  
./plink2 \
  --bfile ukb_cal_allChrs \
  --maf 0.01 --mac 100 --geno 0.1 --hwe 1e-15 \
  --mind 0.1 \
  --write-snplist --write-samples --no-id-header \
  --out qc_pass

 regenie \
  --step 1 \
  --bed ukb_cal_allChrs \
  --extract qc_pass.snplist \
  --keep qc_pass.id \
  --phenoFile ukb_phenotypes_BT.txt \
  --covarFile ukb_covariates.txt \
  --bt \
  --bsize 1000 \
  --out ukb_step1_BT

regenie \
  --step 2 \
  --bgen ukb22828_c#_b0_v3.bgen \
  --ref-first \
  --sample ukb22828_c#_b0_v3.sample \
  --phenoFile ukb_phenotypes_BT.txt \
  --covarFile ukb_covariates.txt \
  --bt \
  --firth --approx --pThresh 0.01 \
  --pred ukb_step1_BT_pred.list \
  --bsize 400 \
  --no-split \
  --out ukb_step2_BT_chr#
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
library("TwoSampleMR")
library(dplyr)

for (i in 446:858){
gut_file <- paste("/gut_bt/GCST90027",i,"_buildGRCh37_5p.tsv",sep="")
gut_exp_dat01 <- read_exposure_data(
    filename = gut_file,
    sep = "\t",
    snp_col = "variant_id",
    beta_col = "beta",
    se_col = "standard_error",
    effect_allele_col = "effect_allele",
    other_allele_col = "other_allele",
    eaf_col = "effect_allele_frequency",
    pval_col = "p_value",
)
gut_exp_dat <- clump_data(gut_exp_dat01, clump_r2 = 0.01, pop = "EUR")
gut_exp_dat$exposure <- paste("gut",i,sep="")

anx_file <- "/chr_qt/ukb_pqt_allchr.regenie"
anx_outcome_dat01 <- read_outcome_data(
    snps = gut_exp_dat$SNP,
    filename = anx_file,
    sep = "\t",
    snp_col = "ID",
    beta_col = "BETA.Y1",
    se_col = "SE.Y1",
    effect_allele_col = "ALLELE1",
    other_allele_col = "ALLELE0",
    eaf_col = "A1FREQ",
    pval_col = "P",
)
anx_outcome_dat <- clump_data(anx_outcome_dat01, clump_r2 = 0.01, pop = "EUR")
anx_outcome_dat <- select(anx_outcome_dat, -id.exposure)
anx_outcome_dat$outcome <- "anxiety"

dat <- harmonise_data(
    exposure_dat = gut_exp_dat,
    outcome_dat = anx_outcome_dat
)

res <- mr(dat)
het <- mr_heterogeneity(dat, method_list = c("mr_two_sample_ml","mr_egger_regression", "mr_ivw","mr_ivw_radial","mr_uwr"))
a <- paste("mr_5pqt",i,sep="")
b <- paste("het_5pqt",i,sep="")
write.table(res,a,row.names=FALSE,col.names=TRUE,sep="\t")
write.table(het,b,row.names=FALSE,col.names=TRUE,sep="\t")
}
```