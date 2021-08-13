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