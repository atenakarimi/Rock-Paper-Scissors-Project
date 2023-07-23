import numpy as np
from playsound import playsound
import platform

def print_color(text, color):
    print(f"\033[{color}m{text}\033[0m")

def get_user_choice():
    while True:
        user_inp = input('What is your choice (Rock/Paper/Scissors)? ').capitalize()
        if user_inp in ['Rock', 'Paper', 'Scissors']:
            return user_inp
        else:
            print_color('Invalid choice. Please enter Rock, Paper, or Scissors.', '31')

def play_sound_effect(song_file_path):
    if platform.system() == 'Darwin':  # macOS
        playsound(song_file_path)
    elif platform.system() == 'Windows':
        # Windows requires the winsound library for .wav files
        import winsound
        winsound.PlaySound(song_file_path, winsound.SND_FILENAME)

def play_round(user_choice):
    choices = np.array(["Rock", "Paper", "Scissors"])
    cp_choice = np.random.choice(choices)
    print_color(f"Computer choice is: {cp_choice}", '33')
    
    if user_choice == cp_choice:
        print_color('Tie', '36')
        play_sound_effect('sounds/tie.wav')  # play sound effect for the tie round
        return 'Tie'
    elif (user_choice == 'Rock' and cp_choice == 'Paper') or \
            (user_choice == 'Paper' and cp_choice == 'Scissors') or \
            (user_choice == 'Scissors' and cp_choice == 'Rock'):
        print_color('You lose this round', '31')
        play_sound_effect(",,,/lose.wav")  # play sound effect for the loser of this round
        return 'Computer'
    else:
        print_color('You win this round', '32')
        play_sound_effect(".../win.wav")   # play sound effect for the winner of this round
        return 'User'

def print_score(user_score, cp_score):
    print_color(f"Current score: User {user_score} - Computer {cp_score}", '34')


def main():
    num = int(input("How many rounds do you want to play? "))

    score_cp = 0
    score_user = 0
    round_number = 1

    while True:
        print_color(f"\nRound {round_number}", '34')
        user_choice = get_user_choice()
        winner = play_round(user_choice)

        if winner == 'User':
            score_user += 1
        elif winner == 'Computer':
            score_cp += 1

        print_score(score_user, score_cp)

        if score_user == num or score_cp == num:
            break

        round_number += 1

    if score_user > score_cp:
        play_sound_effect(".../win_game.wav")  # Play sound effect for the winner
        print_color('Congratulations! You win!!!', '32')
    elif score_user < score_cp:
        play_sound_effect(".../lose_game.wav")  # Play sound effect for the loser
        print_color('Computer wins, you lose!', '31')


if __name__ == "__main__":
    main()
