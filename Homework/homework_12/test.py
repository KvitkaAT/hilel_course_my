import re


def delete_html_tags(text: str) -> str:
    cleaned_tags_text = re.sub(r"<[^>]*>", "", text)
    cleaned_lines_text = re.sub(r"\n\s*\n", "\n", cleaned_tags_text)
    return cleaned_lines_text


print(delete_html_tags("<script>alert('Hello!');</script>\n\n"))


