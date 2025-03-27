exemplu = "After the unexpected death of the Pope, Cardinal Lawrence is tasked with managing the covert and ancient ritual of electing a new one. Sequestered in the Vatican with the Catholic Church’s most powerful leaders until the process is complete, Lawrence finds himself at the center of a conspiracy that could lead to its downfall..."

if "..." in exemplu:
    exemplu_nou = exemplu.replace("...", ".")
print(exemplu_nou)
