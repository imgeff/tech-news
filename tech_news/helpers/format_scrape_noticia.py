from typing import List


def format_comments_count(comments_count: str | None):
    if type(comments_count) == str:
        comments_count_no_spaces: str = comments_count.strip()[0]
        number_of_comments: int = int(comments_count_no_spaces)
        return number_of_comments
    return 0


def format_summary(summary_no_format: List[str]):
    summary: str = ""
    for text in summary_no_format:
        summary += text
    return summary.strip()
