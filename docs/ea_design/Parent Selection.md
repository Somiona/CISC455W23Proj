# Parent Selection
For parent selection, it is a combination of generational and multi-pointer selection.

Since we want to treat a generation as a time interval (day/week/month/year), we are having generational which means all individual will be selected as everyone is experiencing the "new me" replace "old me".

Multi-pointer selection occurs when an individual reach its death age which means it's throwing away and in order to maintain the fixed population size, we need to perform parent selection.

Our thought is to have a random selection of 2-10 individuals as parents and produce an individual that is "average" of the parents.

As we are introducing a new individual with assets appear out of thin air into the population, it somewhat mimic the inflation and a representation as this EA algorithm as an open system.

For multi-pointer selection, we decide to first rank individuals' assets into 5 classes: low, med-low, medium, med-high, high. Second, based on the pointes, we will random select individuals from the classes.

