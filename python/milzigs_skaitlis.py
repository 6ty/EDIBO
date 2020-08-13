#! /usr/bin/python3.6

print("Ievadiet skaitli")
# a=2**20000

#te ir trīs darbības - vertības sagaidīšana, vērtības pārveidošana, piešķirš$
#argument = input()
#a = int(arguments)

#pildot int(input()) "bez izmēginajuma" programma var vienkārši izlidot ...
#tapec lai "nelidotu", mēs izmantosim try ... except .. finally konstrukci$
paziime = False
while not paziime:
#while paziime == False:
#while paziime!=True:
    try:
	    a = int( input() )
	    paziime = True
    except:
	    print("Diemžēl, cinījamais lietotāj, to kas ievadīts nevar parveidot par veselo tipa skaitli")
	    print("Lūdzu ievadiet s_k_a_i_t_l_i vēlreiz")

#if (a == int): print("a**100")
#ja jau ļoti grībās, tad var salīdzinat type(a) == int -> rezultāts būs True
if (a == 5):
	print(a**100)
	print("Aprekins ir gatavs")
print("Šīs teksts atrodas arpus darbību bloka - pierakstīts bez",\
" atstarpēm priekšā, tapēc tas parādīsies jebkurā gadījumā")
#print ("Ievdaiet skaitli")
