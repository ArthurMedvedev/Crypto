# -*- coding: utf-8 -*-
from frequency import generate_list_for_frequency_analyse, generate_frequency_dict_and_write_to_file, generate_frequency_dict


def break_notepad(text: str, d: dict = {}) -> str:
    lst = generate_list_for_frequency_analyse()
    lst_from_txt = generate_list_for_frequency_analyse(generate_frequency_dict(text))

    notepad = generate_notepad_from_two_lists(lst, lst_from_txt)
    notepad = modificate_dict(notepad, d)

    #return encrypt(text, notepad)


def generate_notepad_from_two_lists(lst1: list, lst2: list) -> dict:
    return {k: v for v, k in zip(lst1, lst2)}


def modificate_dict(notepad: dict, d: dict):

    for key, value in d.items():
        notepad_reversed = {v: k for k, v in notepad.items()}
        orignal_letter = notepad_reversed[value]
        notepad[orignal_letter] = notepad[key]
        notepad[key] = value

    print(notepad)

    return notepad
