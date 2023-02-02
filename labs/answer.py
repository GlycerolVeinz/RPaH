# Lenka, 33yo, Female
# not married, smart, straightforward
# studied philosophy at university
# interests: discrimination, social justice, demonstrations against atom weaponry

# Task: Decide propability of these statements:
# a) she is a feminist
# b) she is a bank clerk and a feminist
# c) she is a bank clerk

# By research I evaluate this as a Tversky & Kahneman problem with a little expantion

feminism_propability = 0
bankclerk_propability = 0
bank_feminist_propability = 0
# let's set these values to 0 and we will add 10% (0.1) to any if Lenka's character trait benefits the propability
# to get bank_feminist_propability we need to multiply feminism_propability * bankclerk_propability as the rules of combinatoric multiplication say


banking_traits = "33yo smart studiet_at_uni there_are_more_bankers_then_feminists against_weaponry".split(" ")
feminist_traits = "not_married straightforward social_justice discrimination".split(" ")
#propabilities taken from google search, first link, for simplicity's sake

feminism_propability = len(feminist_traits) / 10
bankclerk_propability = len(banking_traits) / 10
bank_feminist_propability = feminism_propability * bankclerk_propability
#evaluation of propabilities in to number form

if feminism_propability > bankclerk_propability:
    print("a")
    print("c")
    print("b")

else:
    print("c")
    print("a")
    print("b")
# no need to check if b is the biggest because multiple of numbers that are in (0;1) interval will be smaller then the starting numbers
