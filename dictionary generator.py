def create_js_dictionary(words):
    js_code = "const dictionary = {\n"
    for word, part_of_speech in words.items():
        js_code += f'"{word}": "{part_of_speech}",\n'
    js_code += "}\n"
    print(js_code)


if __name__ == "__main__":
    words = {}

    while True:
        user_input = input("Enter word and its part of speech (word part_of_speech), type 'stop' to finish: ")
        if user_input.lower() == "stop":
            create_js_dictionary(words)
            break
        else:
            try:
                word, part_of_speech = user_input.split()
                words[word] = part_of_speech
                create_js_dictionary(words)
            except ValueError:
                print("Invalid input format. Please use 'word part_of_speech' format.")
                continue
