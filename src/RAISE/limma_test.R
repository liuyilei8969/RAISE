# Load required libraries
library(optparse)
library(limma)

# Define command-line arguments
option_list <- list(
  make_option("--as", type="character", help="Input AS matrix (PSI values, tab-delimited)"),
  make_option("--group", type="character", help="Sample group file (two columns: sample and group)"),
  make_option("--output", type="character", help="Output result file")
)

# Parse options
opt_parser <- OptionParser(option_list=option_list)
opt <- parse_args(opt_parser)

# Load AS matrix and group file
as_matrix <- read.table(opt$as, header = TRUE, sep = "\t", row.names = 1)
group_info <- read.table(opt$group, header = TRUE, sep = "\t")

# Match sample names between matrix and group file
samples <- intersect(colnames(as_matrix), group_info$sample)
as_matrix <- as_matrix[, samples]
group_info <- group_info[match(samples, group_info$sample), ]

# Construct design matrix
group_factor <- factor(group_info$group)
design <- model.matrix(~ group_factor)

# Fit linear model
fit <- lmFit(as_matrix, design)
fit <- eBayes(fit)

# Extract result (assumes group_factor has 2 levels)
res <- topTable(fit, coef = 2, number = Inf)
res$event_id <- rownames(res)
res$IncLevelDifference <- res$logFC
res$PValue <- res$P.Value
res$FDR <- res$adj.P.Val

# Save output
write.table(res[, c("event_id", "IncLevelDifference", "PValue", "FDR")],
            file = opt$output, sep = "\t", quote = FALSE, col.names = NA)

cat("Result saved to:", opt$output, "\n")
