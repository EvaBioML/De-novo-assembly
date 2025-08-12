library(ggpubr)
library(readxl)
rm(list = ls())
library(ggplot2)
res <- read.table(choose.files("a.txt"),header = TRUE) 
dfdata = data.frame(res)
colnames(dfdata)
ma<- ggmaplot(dfdata,
         main = expression(""),
         fdr = 0.05, 
         fc = 2, 
         size = 0.4,
         palette = c("#B31B21", "#1465AC", "darkgray"),
         genenames = as.vector(dfdata$name),
         ggtheme = ggplot2::theme_minimal(),
         top = 0,
         select.top.method = c("padj", "fc"),
         label.rectangle = T,
         label.select = c(),)
#作圖
ggmaplot(dfdata,#????u?? 
         main = expression(""),
         fdr = 0.05, 
         fc = 2, 
         size = 0.4,
         palette = c("#B31B21", "#1465AC", "darkgray"),
         genenames = as.vector(dfdata$name),
         ggtheme = ggplot2::theme_minimal(),
         top = 0,
         select.top.method = c("padj", "fc"),
         label.rectangle = T,
         label.select = c(),)
table <- ma$data


###列出up和down的基因
# 設置閾值
fdr_threshold <- 0.05  # FDR閾值
fc_threshold <- 2  # fold change閾值

# 篩選出上調 (up-regulated) 基因：padj < 0.05 且 fc > 2
up_genes <- dfdata[dfdata$padj < fdr_threshold & dfdata$log2FoldChange > fc_threshold, ]

# 篩選出下調 (down-regulated) 基因：padj < 0.05 且 fc < -2
down_genes <- dfdata[dfdata$padj < fdr_threshold & dfdata$log2FoldChange < -fc_threshold, ]

# 列出篩選結果
cat("Up-regulated genes:\n")
write.table(up_genes, "up_genes.txt", sep = "\t", quote = FALSE, row.names = TRUE, col.names = TRUE)

print(up_genes)

cat("\nDown-regulated genes:\n")
write.table(down_genes, "down_genes.txt", sep = "\t", quote = FALSE, row.names = TRUE, col.names = TRUE)







