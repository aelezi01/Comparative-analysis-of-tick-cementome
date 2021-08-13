# initiate project using the virtual environment
renv::init()
renv::restore()
renv::snapshot()

# install packages if necessary 
# renv::install('tidyverse')
# renv::install('here')

# import packages
library(tidyverse)
library(here)

# import dataset
all_orthogroups <- read_tsv(here('data', 'orthofinder_results', 'MC', 'Orthogroups.tsv'))

# remove empty values
all_orthogroups <- na.omit(all_orthogroups)

# save table 
write.csv(all_orthogroups, file = here('data', 'orthofinder_results', 'MC', "shared_orthogroups.csv"), row.names = FALSE )
