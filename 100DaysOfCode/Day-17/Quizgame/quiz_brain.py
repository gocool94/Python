#question_number = 0
#question_list

#next_question()

class QuizBrain():
    def __init__(self,q_list):
        self.question_number = 0
        self.Question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.Question_list[self.question_number]
        self.question_number+=1
        user_answer = input(f"Q {self.question_number} :{current_question.text}  True/False")
        self.check_answer(user_answer,current_question.answer)
        print(f"Your score is {self.score}/{self.question_number}")


    def still_has_questions(self):
        if(self.question_number <len(self.Question_list)):
            return True
        else:
            return False

    def check_answer(self,user_answer,current_answer):
        if(user_answer.lower() == current_answer.lower()):
            print("You got it correct")
            self.score+=1
        else:
            print("you got it wrong")

        print(f"The correct answer is {current_answer}")





