from logic2 import *

#Question 1 answers 
#1
carrots = Symbol("carrots")
orange = Symbol("orange")
knowledge_for_question1 = And(
    Implication(carrots, orange)
)
#2
person = Symbol("person")
vegetarian = Symbol("vegetarian(x)")
like = Symbol("like")
like_person_carrots = Symbol("like(x, carrots)")
knowledge_for_question2 = And(Implication(vegetarian, like_person_carrots))
#3
pass_exam = Symbol("pass(x)")
study_hard = Symbol("study_hard(x)")
knowledge_for_question3 = Implication(study_hard, pass_exam)
#4
Pass = Symbol("? pass(who)")
knowledge_for_question4 = And(Pass)
#5
teaches = Symbol("? teaches(course, which)")
knowledge_for_question5 = And(teaches)
#6
x = Symbol("x")
y = Symbol("y")
enemies = Symbol(f"enemies({x}, {y})")
hates = Symbol(f"hates({x}, {y})")
fight = Symbol(f"fight({x}, {y})")
knowledge_for_question6 = And(Implication(enemies, And(hates, fight)))
