# Naam: Bart Jolink
# Datum: 13-11-2018
# Versie: 1.0

# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein proefstukje van het bestand, met 5 tot 10 fasta's. Ga je runnen met het echte bestand, geef je programma dan even de tijd.

def main():
    bestands_naam = "alpaca_test.tt"
    try:
        headers, seqs = lees_inhoud(bestands_naam)

        zoekwoord = input("Geef een zoekwoord op: ")
        for i in range(len(headers)):
            if zoekwoord in headers[i]:
                print("Header:", headers[i])
                check_is_dna = Is_Dna(seqs[i])
                if check_is_dna:
                    print("Sequentie is DNA")
                    knipt(seqs[i])
                else:
                    print("Sequentie is geen DNA. Er is iets fout gegaan.")

    except TypeError:
        print("Bestand kon niet gevonden worden")
    except FileNotFoundError:
        print("Het bestand kan niet gevonden worden. Zet een geldig fasta bestand in dezelfde map als waar u het programma vanuit draait en probeer het dan opnieuw.")
    except IOError:
        print("Het bestand kan niet geopend worden. Zet een geldig fasta bestand in dezelfde map als waar u het programma vanuit draait en probeer het dan opnieuw")
    except:
        print("Onbekende fout, raadpleeg systeembeheerder")

def lees_inhoud(bestands_naam):
    bestand = open(bestands_naam, "r")
    headers = []
    seqs = []
    seq = ""
    try:
        for line in bestand:
            line = line.strip()
            if ">" in line:
                if seq != "":
                    seqs.append(seq)
                    seq = ""
                headers.append(line)
            else:
                seq += line.strip()
                seqs.append(seq)
    except MemoryError:
        niks = "niks"
    return headers, seqs

def Is_Dna(seq):
    Dna = False
    a = seq.count("A")
    t = seq.count("T")
    c = seq.count("C")
    g = seq.count("G")
    total = a + t + c + g
    if total == len(seq):
        Dna = True
    return Dna


def knipt(alpaca_seq):
    try:
        bestand = open("enzymen.txt")
        for line in bestand:
            naam, seq = line.split(" ")
            seq = seq.strip().replace("^", "")
            if seq in alpaca_seq:
                print(naam, "knipt in sequentie")
    except FileNotFoundError:
        print("Bestand enzymen.txt kon niet gevonden worden")
    except IOError:
        print("Bestand enzymen.txt kon niet geopend worden")



main()
