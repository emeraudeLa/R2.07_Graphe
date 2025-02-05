'''
Classe tp 1-2
'''

class Graphe(object):
    def __init__(self, graphe_dict=None):
        """ initialise un objet graphe.
        Si aucun dictionnaire n'est
        créé ou donné, on en utilisera un
        vide
        """
        if graphe_dict == None:
            graphe_dict = {}
        self._graphe_dict = graphe_dict
        
    def aretes(self, sommet):
        """ retourne une liste de toutes les aretes d'un sommet"""
        return self._graphe_dict[sommet]
    
    def all_sommets(self):
        """ retourne tous les sommets du graphe """
        return set(self._graphe_dict.keys())
    
    def all_aretes(self):
        """ retourne toutes les aretes du graphe
        à partir de la méthode privée,_list_aretes, à définir
        plus bas.
        Ici on fera donc simplement appel à cette méthode.
        """
        return self.__list_aretes()
    
    def add_sommet(self, sommet):
        """ Si le "sommet" n'set pas déjà présent
        dans le graphe, on rajoute au dictionnaire
        une clé "sommet" avec une liste vide pour valeur.
        Sinon on ne fait rien.
        """
        if sommet not in self._graphe_dict:
            self._graphe_dict[sommet] = set()
   
    def add_arete(self, arete):
        """ l'arete est de type set, tuple ou list;
        Entre deux sommets il peut y avoir plus
        d'une arete (multi-graphe)
        """
        if len(arete) == 2:
            sommet1, sommet2 = arete
            if sommet1 in self._graphe_dict:
                self._graphe_dict[sommet1].add(sommet2)
            else:
                self._graphe_dict[sommet1] = {sommet2}
            
            if sommet2 in self._graphe_dict:
                self._graphe_dict[sommet2].add(sommet1)
            else:
                self._graphe_dict[sommet2] = {sommet1}
   
    def __list_aretes(self):
        """ Methode privée pour récupérers les aretes.
        Une arete est un ensemble (set)
        avec un (boucle) ou deux sommets.
        """
        aretes = []
        for sommet, voisins in self._graphe_dict.items():
            for voisin in voisins:
                aretes.append(frozenset([sommet, voisin]))
        return aretes
   
    def __iter__(self):
        """ on crée un itérable à partir du graphe"""
        self._iter_obj = iter(self._graphe_dict)
        return self._iter_obj
   
    def __next__(self):
            """ Pour itérer sur les sommets du graphe """
            return next(self._iter_obj)
   
    def __str__(self):
        res = "sommets: "
        for k in self._graphe_dict:
            res += str(k) + " "
        res += "\naretes: "
        for arete in self.__list_aretes():
            res += str(arete) + " "
        return res

'''
Classe enfant de classe Graphe (mettre la classe parente entre parentheses)
'''
class Graphe2(Graphe):
    def sommet_degre(self, sommet):
        """ renvoie le degre du sommet """
        degre=len(self.aretes(sommet))
        if(sommet in degre):
            degre += 1
        return degre
    
    def trouve_sommet_isole(self):
        """ renvoie la liste des sommets isoles """
        isoles=[]
        sommets=[]
        sommets.append(self.all_sommets())
        for i in range (len(sommets)):
            if(self.arete(sommets[i]==0)):
                isoles.append(sommets[i])
        return isoles
    
    def Delta(self):
        """ le degre maximum """
        max=0
        sommets=[]
        sommets.append(self.all_sommets())
        for i in range (len(sommets)):
            if(self.sommet_degre(sommets[i])>max):
                max = self.sommet_degre(sommets[i])
        return max
    
    def list_degres(self):
        """ calcule tous les degres et renvoie un
        tuple de degres decroissant
        """
        degres=()
        deg=0
        sommets=[]
        sommets.append(self.all_sommets())
        for i in range (len(sommets)):
            deg = self.sommet_degre(sommets[i])
            degres.append(deg)
        return degres

    #def trouve_chaine(self, sommet_dep, sommet_arr, chain=None):
    
    
