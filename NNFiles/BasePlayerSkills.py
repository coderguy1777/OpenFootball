# for calculating the number of passes done by player for pass completion
def passpercent(cp, incp, tcp):
    return cp - incp / tcp

# for calculating the weeks left in a season
def weeksleft(cwk, twk):
    return twk - cwk

# for calculating the percentage of interceptions
# completed by player
def intrcptps(In, Icn, Iincn):
    return Iincn - Icn / In

# for calculating the amount of
# valid touch downs done by a
# given player percent wise
def tdpct(TDc, TDinc, NTd):
    return TDc - TDinc / NTd
