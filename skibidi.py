import random
import time

words = ["skibidi", "toilet", "gyatt", "rizzer", "ohio", "sigma", "fanum tax", "pluh"]

def predict_text(input_str):
    time.sleep(0.5)
    return f"{input_str} {random.choice(words)}"

def main():
    print("enter text (q to quit):")
    while True:
        i = input("> ")
        if i == "q": break
        
        res = predict_text(i)
        print(f"prediction: {res}")

if __name__ == "__main__":
    main()
