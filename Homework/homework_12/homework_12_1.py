import codecs
import re


def delete_html_tags(html_file="draft.html", result_file="cleaned.txt"):
    with codecs.open(html_file, "r", 'utf-8') as file:  # opens the file for reading
        html = file.read()

    cleaned_text = delete_html_tags_from_text(html)
    with codecs.open(result_file, "w", "utf-8") as file:  # opens the file for writing
        file.write(cleaned_text)


def delete_html_tags_from_text(text: str) -> str:
    cleaned_tags_text = re.sub(r"<[^>]*>", "", text)  # deletes tags in a text
    cleaned_lines_text = re.sub(r"\n\s*\n", "\n", cleaned_tags_text)  # deletes empty lines in a text
    return cleaned_lines_text


if __name__ == "__main__":
    delete_html_tags("draft.html", "cleaned.txt")
    print("Ok")
