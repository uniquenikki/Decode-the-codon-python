S=input()
myDict = {' Methionine': ['AUG'], 
          'Phenylalanine': ['UUU', 'UUC'],
          'Leucine': ['UUA', 'UUG'],
          'Serine': ['UCU', 'UCC', 'UCA','UCG ' ],
          'Tyrosine': ['UAU', 'UAC'],
          'Cysteine': ['UGU', 'UGC'],
          'Tryptophan': ['UGG'], 
          'STOP': ['UAA', 'UAG', 'UGA' ]
          }

def search(myDict, lookup):
    for key, value in myDict.items():
        for v in value:
            if lookup in v:
                return key

print(search(myDict, 'UUU'))