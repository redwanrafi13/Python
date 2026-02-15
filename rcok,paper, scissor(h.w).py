import cv2
import mediapipe as mp
import random
import time


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils


player_score = 0
computer_score = 0
choices = ["rock", "paper", "scissors"]


last_player_move = ""
last_computer_move = ""
last_winner = ""
round_active = False
countdown_start = None
countdown_time = 3  # seconds


def get_hand_gesture(hand_landmarks):
    tips_ids = [4, 8, 12, 16, 20]
    fingers = []


    if hand_landmarks.landmark[tips_ids[0]].x < hand_landmarks.landmark[tips_ids[0] - 1].x:
        fingers.append(1)
    else:
        fingers.append(0)


    for id in range(1, 5):
        if hand_landmarks.landmark[tips_ids[id]].y < hand_landmarks.landmark[tips_ids[id] - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)


    if fingers == [0, 0, 0, 0, 0]:
        return "rock"
    elif fingers == [1, 1, 1, 1, 1]:
        return "paper"
    elif fingers == [0, 1, 1, 0, 0]:
        return "scissors"
    else:
        return None


def get_winner(player, computer):
    if player == computer:
        return "Draw"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "Player Wins"
    else:
        return "Computer Wins"


cap = cv2.VideoCapture(0)

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)


        if not round_active:
            countdown_start = time.time()
            round_active = True

        elapsed = time.time() - countdown_start
        remaining = countdown_time - int(elapsed)

        if remaining > 0:
            # Show countdown
            cv2.putText(frame, f"Get Ready: {remaining}", (200, 250),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 4)
        else:

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    gesture = get_hand_gesture(hand_landmarks)
                    if gesture:
                        last_player_move = gesture
                        last_computer_move = random.choice(choices)
                        last_winner = get_winner(last_player_move, last_computer_move)

                        if last_winner == "Player Wins":
                            player_score += 1
                        elif last_winner == "Computer Wins":
                            computer_score += 1

                        round_active = False  
                        break
            else:
                last_player_move = "No Hand"
                last_computer_move = random.choice(choices)
                last_winner = "Computer Wins"
                computer_score += 1
                round_active = False


        cv2.putText(frame, f"Score - Player: {player_score}  Computer: {computer_score}",
                    (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)


        if last_player_move:
            cv2.putText(frame, f"Player: {last_player_move}", (10, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        if last_computer_move:
            cv2.putText(frame, f"Computer: {last_computer_move}", (10, 140),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        if last_winner:
            color = (0, 255, 0) if "Player" in last_winner else ((0, 0, 255) if "Computer" in last_winner else (255, 255, 0))
            cv2.putText(frame, f"Result: {last_winner}", (10, 180),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

        cv2.imshow("Rock Paper Scissors", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
