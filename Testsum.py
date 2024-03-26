def questions(question1, A, B, C, D, answer, wrong1, wrong2, wrong3):
    question_asking = True
    while question_asking:
        print(question1)
        print(f"A. {A}")
        print(f"B. {B}")
        print(f"C. {C}")
        print(f"D. {D}")
        question = input("what is your answer A, B, C or D: ")
        if question == answer:
            print("correct!")
            correct.append(question)
            question_asking = False
        elif question.strip(" ") ==  "":
            print("invalid Answer please enter no blanks")
        elif question == wrong1:
            print(f"incorrect the correct answer was {answer}")
            question_asking = False
        elif question == wrong2:
            print(f"incorrect the correct answer was {answer}")
            question_asking = False
        elif question == wrong3:
            print(f"incorrect the correct answer was {answer}")
            question_asking = False
        else:
            print("You did not enter a valid answer please enter A, B, C or D")
        print(" ")

questions("What is the first element on the periodic table", "Hydrogen", "Helium", "Gold", "Silver", "A", "B", "C", "D")
questions("What is the Fifth element on the periodic table", "Carbon", "Boron", "Helium", "Lithium", "B", "A", "C", "D")
questions("What is the Eighth element on the periodic table", "Silicon", "Fluorine", "Oxygen", "Nitrogen", "C", "A", "B", "D")
questions("What is the eleventh element on the periodic table", "Sodium", "Nitrogen", "Sulfur", "Chlorine", "A", "B", "C", "D")
questions("What is the twentieth element on the periodic table", "Iron", "Bromine", "Sulfur", "Calcium", "D", "A", "C", "A")
questions("What is the tenth element on the periodic table", "Iodine", "Neon", "Titanium", "Zinc", "B", "A", "C", "D")
