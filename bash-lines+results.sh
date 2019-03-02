//bash command line:

for number in {1 2}; do cp file.txt file-$number.txt; done
//result:
//file-{1.txt
//file-2}.txt

for number in {1..2}; do cp file.txt file-$number.txt; done
//result:
//file-1.txt
//file-2.txt

for i in $('ls'); do echo plik czy katalog: $i; done
//results:
//plik czy katalog: Desktop
//plik czy katalog: Documents
//plik czy katalog: Downloads
//plik czy katalog: Music
//plik czy katalog: Pictures
//plik czy katalog: Public
//plik czy katalog: Templates
//plik czy katalog: Videos
//plik czy katalog: VirtualBox
//plik czy katalog: wstep.odt
