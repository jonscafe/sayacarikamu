import os
from datadikti import datadikti as datadikti
from linkedin import run_linkedin_search as linkedin_search
from pddikti import pddikti as pddikti
from scholar import scholar as scholar
from studentmail import run_studentmail_search as run_studentmail_search
from medium import medium as medium
from sinta import sinta as sinta
import sys
import time

def loading_animation():
    chars = "/—\\|"
    for _ in range(20):
        for char in chars:
            sys.stdout.write('\r' + 'chotto matte sebentar dude... ' + char)
            sys.stdout.flush()
            time.sleep(0.1)

def welcomingMsg():
    word = "SayaCariKamu!"
    author_info = "\033[95mauthor: jonscafe / k.eii\033[0m"
    project_info = "soceng project: osint/information gathering tool"

    line_length = len(word) + 6
    half_line_length = (line_length - len(word)) // 2

    separator_line = "=" * half_line_length
    centered_word = f"{separator_line} {word} {separator_line}"
    centered_author_info = f"{separator_line} {author_info} {separator_line}"
    centered_project_info = f"{separator_line} {project_info} {separator_line}"

    print(centered_word)
    print(centered_author_info)
    print(centered_project_info)

def main():
    welcomingMsg()
    print('')
    user_input = input("inputNama: ")
    loading_animation()
    print('')
    print('=========================')

    datadikti(user_input)
    pddikti(user_input)
    linkedin_search(user_input)
    scholar(user_input)
    run_studentmail_search(user_input)
    medium(user_input)
    sinta(user_input)

if __name__ == "__main__":
    main()
