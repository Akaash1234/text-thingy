import random
import time

# text prediction thingy
words = ["skibidi", "toilet", "gyatt", "rizzer", "ohio", "sigma", "fanum tax", "pluh"]

def predict_text(input_str):
    # complex ai logic here
    time.sleep(0.5) # thinking...
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
