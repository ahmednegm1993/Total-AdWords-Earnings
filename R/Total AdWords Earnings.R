library(readxl)
library(dplyr)

file_path <- "E:\\Data_analysis_projects\\Total AdWords Earnings\\dataset\\google_adwords_earnings.xlsx"
data <- read_excel(file_path)

total_earnings <- data %>%
  group_by(business_type) %>%
  summarize(total_adwords_earnings = sum(adwords_earnings, na.rm = TRUE))

print(total_earnings)
