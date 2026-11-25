## Definisi Kelas ##
## Definisi Kelas TreeElmt
## Nama: Khresna Mulia Putra (Khresmupu)
## NRP: 2572032

## Definisi Atribut:
#   value       : Atribut ini akan menyimpan 
#                 nilai dari element(str)
#   childrenCount: Atribut ini akan menyimpan 
#                 nilai dari element(str)
#   children       : Atribut ini akan menyimpan 
#                 nilai dari element(str)
class TreeElmt:
    def __init__(self,nilai,ukuran):
        self.value=nilai
        self.childrenCount=0
        self.children=[None]*ukuran
    def printTree(self,root,depth):
        print(" " * depth,root.value)
        for i in range(root.childrenCount):
            self.printTree(root.children[i],depth + 1)
        return
    def addChild(self,child):
        if self.childrenCount<len(self.children):
            self.children[self.childrenCount]=child
            self.childrenCount+=1
        return
    def findNode(self,root,target):
        if root.value==target:
            return True
        for i in range(root.childrenCount):
            if self.findNode(root.children[i],target):
                return True
        return False
            
# Kamus Data (Main Program):
# p             : Gambaran objek list angka 
#                   (TreeElmt)
def main():
    p=TreeElmt("B",2)
    p.addChild(TreeElmt("A",2))
    p.children[0].addChild(TreeElmt("D",2))
    p.children[0].children[0].addChild(TreeElmt("H",2))
    p.children[0].children[0].addChild(TreeElmt("I",2))
    p.children[0].addChild(TreeElmt("F",2))
    p.children[0].children[1].addChild(TreeElmt("J",2))
    p.children[0].children[1].addChild(TreeElmt("K",2))
    p.addChild(TreeElmt("C",2))
    p.children[1].addChild(TreeElmt("G",2))
    p.children[1].children[0].addChild(TreeElmt("L",2))
    p.children[1].children[0].addChild(TreeElmt("M",2))
    p.children[1].addChild(TreeElmt("E",2))
    p.children[1].children[1].addChild(TreeElmt("N",2))
    p.children[1].children[1].addChild(TreeElmt("O",2))
    p.printTree(p,0)
    if p.findNode(p,"K"):
        print("Node K ditemukan")
    else:
        print("Node K tidak ditemukan")
    if p.findNode(p,"A"):
        print("Node A ditemukan")
    else:
        print("Node A tidak ditemukan")
    if p.findNode(p,"Z"):
        print("Node Z ditemukan")
    else:
        print("Node Z tidak ditemukan")
    return
            
if __name__ == '__main__':
    main()