import random
import json
import os

class flashcard:
    def __init__(self,question,answer):
        self.question= question.strip()
        self.answer=answer.strip()
        
    def to_dict(self):
        return{"question",self.question,"question",self.answer}
    
    @staticmethod
    def from_dict(data):
        return flashcard(data["question"],data[answer])
    
class flashcarddeck:
    def __init__(self,filename="flashcard.json"):
        self.cards =[]
        self.filename= filename
        self.load()
        
    def add_card(self,question,qanswer):
        self.cards.append(flashcard(question,answer))
        self.save()
        
    def remove_card(self,index):
        if 0<=index <len(self.card):
            del self.cards[index]
            self.save()
            
    def edit_card(self, index,new_q=None,new_a = None):
        if 0 <= index ,len(self.cards):
            if new_q:
                self.cards[index].question =new_q
            if new_a:
                self.cards[index].answer = new_a
                
    def shuffle(self):
        random.shuffle(self.cards)
        
    def quiz(self,reverse=False):
        score = 0
        wrong_cards=[]
        for card in self.cards:
            q,a=(card.answer,card.question) if reverse else (card.question,card.answer)
            print(f"\nquestion = {q}")
            user_answer= input("your_answer: ").strip()
            
            if user_answer.lower() = a.lower():
                print("Correct!")
                score +=1
                
            else:
                print(f"Wrong! correct answer: {a}")
                wrong_cards.append(card)
                
        print(f"\nQuiz finished! your score: {score}/{len(self.cards)}")
        
        if wrong_cards:
            print("\nYou missed the following cards")
            for c in wrong_cards:
                print(f"- {c.question} → {c.answer}")
                
        def list_cards(self):
            if not self.cards:
                print("No flashcards available")
            for idx,card in enumerate(self.cards,1):
                print(f"{idx}.{card.question} → {card.answer}")
                
        def save(self):
            with open(self.filename,"w") as f:
                json.dump([c.to_dict() for c in self.cards],f,indent=4)
                
        def load(self):
            if os.path.exists(self.filename):
                with open(self.filename,"r") as f:
                    data = json.load(f)
                    self.cards = [flashcard.from_dict(d) for d in data]
                    
                    
def main():
    deck = flashcarddeck()
    
    while True:
        print("\n=====Flashcard=====")
        print("1. Add Flashcard")
        print("2. Viwe all Flashcards")
        print("3. Edit Flashcards")
        print("4. Delete Flashcards")
        print("5. quiz (normal mode)")
        print("6. quiz (reverse mode)")
        print("7. shuffle cards")
        print("8. exit")
        choice = input("choose an option")
        
        if choice== "1":
            q= input("enter question")
            a=input("enter answer")
            deck.add_card(q,a)
        elif choice == "2":
            deck.list_cards()
        elif choice == "3":
            deck.list_cards()
            idx=int(input("enter card number to edit:"))
            new_q =input("new quetion (leave blank to keep):")
            new_a =input("new answer (leave blank to keep):")
            deck.edit_card(idx, new_q or None, new_a or None )
        elif choice == "4":
            deck.list_cards()
            idx = int(input("enter card number to delete: ")) -1
            deck.remove_card(idx)
        elif choice == "5":
            deck.shuffle()
            deck.quiz()
        elif choice == "6":
            deck.shuffle()
            deck.quiz(reverse =True)
        elif choice == "7":
            deck.shuffle()
            print("deck shuffled!")
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            pirnt("invalid input!")
            
            
if __name__ == "__main__":
    main()