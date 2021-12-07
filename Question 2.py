from utils import *
from logic2 import *

#Question 2 answers 
#1
maria = Symbol("maria")
peter_lucas = Symbol("peter lucas")
read = Symbol(f" read ({maria}, logic programming book)")
by = Symbol(f"by ({peter_lucas})")
knowledge_for_question1 = And(Implication(read, by))
#2
is_girl = Symbol("is_girl(x)")
shopping = Symbol("shopping")
like = Symbol(f"like(x, {shopping} )")
knowledge_for_question2 = And(Implication(is_girl, like))
print(knowledge_for_question2)
#3
who = Symbol("?")
knowledge_for_question3  = And(who ,like)
#4
city = Symbol("city(x, big, crowdy)")
hates = Symbol("kirke, x")
knowledge_for_question4 = And(Implication(city, hates))
# print(knowledge_for_question4.formula())


