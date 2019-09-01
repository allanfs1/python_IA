
''' IA  Inteligencia'''
class Nos(object):
    def __init__(self,left = None,right = None):
     self.left = left
     self.right = right
     self.no = None
     self.folhas = []

    def derivar_folhas(self):
        ladA = self.no[0]
        tam = len(ladA)#'Atribuindo tamanho do cccmmm = 6 a variavel tam (tamanho do |cccmmm|)'
    #    for i in range(len("".join(self.no))
        for n1 in range(0,tam-1):#'tam=6 (tam -1) tam=5'
            for n2 in range(0,tam-1):#'(n^2) tam-1 5X5 = 25'
              folha = Nos() # variavel Folha (Atribuindo a folha a um No(Class))
              la = "".join([ladA[i] for i in range(tam) if i != n1 or i != n2])
              folha.no = (la,ladA[n1] + ladA[n2],"")#'acesso a um dos ramos no, e colocando em uma tupla(concatenando ladA[n1] com ladoA[n2].Gerando posibilidades |cccmmm|) '
              self.folhas.append(folha.no)#'Jogando em um vetor'



    def print_folhas(self):
      for x in self.folhas:#'Lendo todas as folhas'
          print(x)#'printando x'

raiz = Nos()#'istanciando'
raiz.no = ["cccmmm","",""]
raiz.derivar_folhas() # derivar folha
raiz.print_folhas()#'print'

#'Posibilidades do primeiro no barco'
#[cccmmm] (POS) = [ [cc,cc,cc,mc,mc],[cc,cc,cc,cm,cm],[cc,cc,cc,cm,cm],[cm,cm,cm,mm,mm],[cm,cm,cm,mm,mm] ]
#"    |   "
#iiiiiiii
#[Cccmmm]
#[cCcmmm]
#[ccCmmm]
#[cccMmm]
#[cccmMm]

#Posibilidades do lado esquerdo
#[cccmmm]
#[cmmm,cmmm,cmmm,ccmm,ccmm],[cmmm,cmmm,cmmm,ccmm,ccmm],
#[cmmm,cmmm,cmmm,ccmm,ccmm],[ccmm,ccmm,ccmm,cccm,cccm],[ccmm,ccmm,cmm,cccm,cccm]
