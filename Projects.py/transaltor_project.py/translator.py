# pip install googletrans==4.0.0-rc1

from googletrans import Translator

# Initialize the Translator
translator = Translator()

# Function to translate text between Hindi and English based on user's choice
def translate_text(text, src_lang, dest_lang):
    try:
        translation = translator.translate(text, src=src_lang, dest=dest_lang)
        print(f"The translation of '{text}' is: '{translation.text}'")
    except Exception as e:
        print("Sorry, there was an error translating the text:", e)

# Main program
while True:
    print("\nWelcome to the Hindi-English Translator!")
    print("1. Translate Hindi to English")
    print("2. Translate English to Hindi")
    print("3. Exit")
    choice = input("Enter your choice (1/3): ")

    if choice == '1':
        hindi_text = input("Enter the Hindi word or sentence: ")
        translate_text(hindi_text, src_lang='hi', dest_lang='en')
    elif choice == '2':
        english_text = input("Enter the English word or sentence: ")
        translate_text(english_text, src_lang='en', dest_lang='hi')
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
