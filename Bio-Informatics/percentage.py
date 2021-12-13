from operator import eq
seq1 = "ASCSNRCKCPRDT"
seq2 = "ADCNSR--LCRPM"
seq1 = list(seq1)
seq2 = list(seq2)
print(seq1)
print(seq2)

#To find identity between the two sequences
a = sum(map(eq, seq1, seq2))
identity = print("Identity: ", a)

#To find similarity 
count = 0
for i in range(len(seq1)):
    if (seq1[i] == "S" and seq2[i] == "N" or seq1[i] == "N" and seq2[i] == "S" or seq1[i] == "D" and seq2[i] == "P" 
        or seq1[i] == "P" and seq2[i] == "D"):
        count += 1
sim = print("Similarity:", count)

# To find Obtained match
# Obtained match  = Similarity + Identity
obt_match = a + count
print("Obtained match: ", obt_match)

# Length of the sequence
if(len(seq1) == len(seq2) or len(seq1) > len(seq2)):
    print("Total length: ", len(seq1))
grt_seq = len(seq1)

if(len(seq2) > len(seq1)):
    print("Total length: ", len(seq2))
grt_seq = len(seq2)

# To find gap between the sequences
cnt = 0
for i in range(len(seq1)):
    if seq1[i] == "-":
        cnt += 1
    elif(seq2[i] == "-"):
        cnt += 1
print("Gap: ", cnt)

# To find Total
# Total = Total length - Gap
total = grt_seq - cnt
print("Total: ", total)

# To find Percentage of match between the sequences
# Percentage = (Obtained match / Total) * 100
percent_match = (obt_match / total) * 100
print("Percentage of match: ", percent_match)
