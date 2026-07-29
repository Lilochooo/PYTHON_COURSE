# Python, From a C Programmer's Perspective

Built for someone who already knows C — functions, arrays, structs, pointers,
`scanf`/`printf`, control flow. This course leans on that background instead
of re-teaching "what is a variable."

## How this course is structured

Each module folder has three files:

- `lesson.md` — the concept, explained, with C comparisons where they help
- `exercises.py` — TODOs for you to fill in (this is where you actually learn)
- `solutions.py` — reference answers, don't peek until you've tried

Work through modules in order. Each one assumes the last.

```
01-basics/           variables, types, I/O, no more semicolons or braces
02-control-flow/     if/elif/else, while, for, and why Python's for is different
03-data-structures/  lists, tuples, dicts, sets — Python's answer to arrays/structs
04-functions/        def, default args, *args/**kwargs, return values
05-oop/              classes — Python's version of structs + function pointers
06-files-modules/    reading/writing files, imports, organizing multi-file projects
07-mini-projects/    project ideas to combine everything
```

## Setting this up in Cursor

1. Open the `python-course` folder in Cursor (`File > Open Folder`).
2. Make sure Python is installed (`python --version` or `python3 --version`
   in Cursor's terminal). If not, install from python.org.
3. To run any exercise file, open it and either:
   - hit the "Run Python File" button (top right), or
   - in the terminal: `python 01-basics/exercises.py`
4. Use Cursor's inline chat (Cmd/Ctrl+K) on a TODO block if you get stuck and
   want a hint — but try first. Read `lesson.md` before touching `exercises.py`.

## Suggested pace

Modules 1–4 are the core of the language — don't rush these, they're where the
new mental model (dynamic typing, no manual memory management, indentation as
syntax) actually clicks. Modules 5–6 are more "here's how Python organizes
larger programs." Module 7 is where it stops feeling like an exercise sheet.

Start with `01-basics/lesson.md`.
