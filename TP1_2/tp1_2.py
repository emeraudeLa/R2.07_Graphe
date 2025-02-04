#import mygraph as gr

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

"""
Une classe Python pour creer et manipuler des graphes
"""
if __name__ == "__main__":
    graphe = {"A" :{"C"},
        "B" : {"C", "E"},
        "C" : {"A", "B", "D", "E"},
        "D" : {"C"},
        "E" : {"C", "B"},
        "F" : {}
    }
    g = Graphe(graphe)
    print(g.aretes("A"))
    print(g.all_sommets)
    print(g.all_aretes)
    
    #print(g.__list_aretes)
