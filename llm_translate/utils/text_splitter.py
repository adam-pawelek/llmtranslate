import re



def get_first_n_words(text: str, n_words) -> str:
    words = re.split(r'\s+', text)
    words = words[0:n_words]
    return ' '.join(words)



def split_text_to_chunks(text, max_lenght):
    global WORD_TOKEN_MULTIPLY
    splited_text = re.split(r'\s+', text)
    last_comma_index = -1
    last_dot_index = -1
    last_index = 0
    chunks_of_text = []


    for index, word in enumerate(splited_text):
        if "," in word:
            last_comma_index = index
        if "." in word or "?" in word or "!" in word:
            last_dot_index = index

        if (index - last_index + 1) >= max_lenght:
            if last_dot_index >= last_index:
                chunks_of_text.append(splited_text[last_index:last_dot_index + 1])
                last_index = last_dot_index + 1
            elif last_comma_index >= last_index:
                chunks_of_text.append(splited_text[last_index:last_comma_index + 1])
                last_index = last_comma_index + 1
            else:
                chunks_of_text.append(splited_text[last_index:index+1])
                last_index = index + 1

    # Add the last chunk
    if last_index < len(splited_text):
        chunks_of_text.append(splited_text[last_index:])

    # Verify the chunks
    check_sentence = [word for chunk in chunks_of_text for word in chunk]

    for index, word in enumerate(check_sentence):
        if word != splited_text[index]:
            print("Error Error")

    return [" ".join(chunk) for chunk in chunks_of_text]