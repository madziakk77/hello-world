//bash command line:

for number in {1 2}; do cp file.txt file-$number.txt; done
//result:
//file-{1.txt
//file-2}.txt
for number in {1..2}; do cp file.txt file-$number.txt; done
//result:
//file-1.txt
//file-2.txt
