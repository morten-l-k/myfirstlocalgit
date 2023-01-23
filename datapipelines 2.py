import csv
#Opgave A
class Step:
    def apply(self,input) :
        """
        A method which takes an argument and returns a result
        """
        return input
    def description(self) -> str:
        """
        A method which returns a string descriping what a step does
        """
        return self.__doc__.lower()

class AddConst(Step):
    def __init__(self,constant):
        self._constant = constant
    def apply(self,input):
        return self._constant + input
    def description(self) -> str:
        return 'Add ' + str(self._constant)

class Repeater(Step):
    def __init__(self,num:int):
        self._num = num
    def apply(self,input:int):
        if isinstance(input,int):
            if self._num <= 0:
                return []
            else:
                return [input]*self._num
        else: raise ValueError('Value is not an int')
    def description(self) -> str:
        return 'Repeat ' + str(self._num) + ' times, as a list'
        
class GeneralSum(Step):
    def __init__(self,neutral_elm,operator):
        self._operator = operator
        self._neutral_elm = neutral_elm
    def apply(self,input:list):
        sum = self._neutral_elm
        for i in input:
            sum = self._operator (sum,i) 
        return sum
    def description(self) -> str:
        return 'GeneralSum is a parent class to SumSum and ProductNum. It returns the sum depending on the class instantiated'
        
class SumNum(GeneralSum):
    def __init__(self) -> None:
        super().__init__(0,(lambda x,y : x + y))
    def description(self) -> str:
        return 'Sum all elements'

class ProductNum(GeneralSum):
    def __init__(self) -> None:
        super().__init__(1,(lambda x,y : x*y ))
    def description(self) -> str:
        return 'Multiply all elements'


# con1 = AddConst(4)
# print(con1.apply(6))
# print(con1.description())
# rep1 = Repeater(4)
# rep1.apply(4)
# print(rep1.description())
# sum1 = SumNum()
# prod1 = ProductNum()
# print(sum1.apply([1,2,3,4]))
# print(prod1.apply([1,2,3,4]))

#Opgave B
class Map:
    def __init__(self,step):
        self._step = step
    def apply(self,input:list):
        if isinstance(input,list):
            tmp = []
            for i in input:
                tmp.append(self._step.apply(i))
            return tmp
        else:
            raise ValueError(str(input) + ' is not a list. Input needs to be a list')
    def description(self) -> str:
        return 'add ' + str(self._step.description())

map1 = Map(SumNum())
# print(map1.apply([[7,4,2,5]]))
# print(map1.description())

#Opgave C
class Pipeline(Step):
    def __init__(self,lst:list):
        self._lst = lst
    def apply(self,startSum):
        try:
            tmp = startSum
            for i in self._lst:
                obj = i
                tmp = obj.apply(tmp)
            return tmp
        except:
            print('There was an error in class: ', i.description())
    def description(self):
        tmp = ''
        for i in self._lst:
            word = i.description()
            tmp = tmp + word + ' -> '
        return '[' + tmp + 'OPERATION FINISHED]'
    def add_step(self,step):
        self._lst.append(step)

pipeline = Pipeline([AddConst(45),Repeater(3),Map(AddConst(-3))])

print('Result is: ', pipeline.apply(0))
pipeline.add_step(SumNum())
print('Result is: ', pipeline.apply(0))
print(pipeline.description())

#Opgave D
class CsvReader(Step):
    def apply(self,filename:str) -> list:
        tmp = []
        with open(filename,'r') as file:
            reader = csv.reader(file)
            (name,col,hp) = list(reader)[0]
            file.seek(0)
            for x in list(reader)[1::]:
                tmp.append({name:x[0],col:x[1],hp:x[2]})
        return tmp
    def description(self):
        return 'Returns a list of dictionaries'

obj = CsvReader()
critterDict = obj.apply('critters.csv')

class CritterStats(Step):
    def apply(self,dict_list:list) -> dict:
        tmp = {}
        for x in dict_list:
            if x['Colour'] in tmp:
                tmp[x['Colour']] += 1
            else:
                tmp[x['Colour']] = 1
        return tmp

critterStat = CritterStats()
# numbersInCrit = critterStat.apply(critterDict)

class ShowAsciiBarchart(Step):
    def apply(self,dictionary):
        for key,value in dictionary.items():
            print(f'{key:12}' + ':'+ str('*'*value))
        return dictionary

tmpObj = ShowAsciiBarchart()

class Square(Step):
    def apply(self,input):
        if isinstance(input,(int,float)):
            return input*input
        elif isinstance(input,list):
            tmp = []
            for i in input:
                tmp.append(i*i)
            return tmp
        else:
            raise Exception('Input is not valid to square')

squareSome = Square()
print(squareSome.apply([4,5]))
#Trying to add a new line to see changes in VSC
print(squareSome.apple([1,2,3]))