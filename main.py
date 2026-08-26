import os
import time
import sys

# ==============================
# PROJECT 190825
# COLOR SYSTEM
# ==============================

RESET = "\033[0m"

GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"
BOLD = "\033[1m"


# ==============================
# BASIC FUNCTIONS
# ==============================

def clear():
    os.system("clear")


def pause(seconds=1):
    time.sleep(seconds)


def type_text(text, color=WHITE, speed=0.025):
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(speed)
    print()


def divider():
    print(CYAN + "====================================" + RESET)


# ==============================
# PROJECT START
# ==============================

clear()

type_text("> INITIALIZING PROJECT_190825...", GREEN)
pause(0.6)

type_text("> Loading encrypted file...", GREEN)
pause(0.8)

print()

type_text("This file was created", WHITE)
type_text("for one particular person and the person is u Bi****i.", MAGENTA)
pause(1)

print()

type_text("> SYSTEM CHECK...", CYAN)
pause(0.5)

type_text("> CONNECTION DATA FOUND ✓", GREEN)
pause(0.5)

type_text("> DATE: 19.08.2025", YELLOW)
pause(0.5)

type_text("> MEMORY COUNT: 365 DAYS", YELLOW)
pause(1)

print()

divider()

print(CYAN + BOLD + "          PROJECT: 365" + RESET)
print(CYAN + "          FILE ID: 190825" + RESET)
print(GREEN + "          STATUS: ACTIVE" + RESET)
print(YELLOW + "          ACCESS: RESTRICTED" + RESET)

divider()

pause(1)

print()

type_text("Something is hidden inside... 👀", YELLOW)
pause(1)

print()

type_text("[Ei software-t unlock koribole aru level-up hobole, mur kisu kotha hunibo lagibo...]", GREEN)

print()

type_text("Bhalke huniba, karon protitu level-or pichot eta eta kotha lukai ase. 👀", YELLOW)

print()

type_text("Ready ne?", MAGENTA)

choice = input(
    "\n" + CYAN + "Jodi ready asa, then OPEN type kora..." + RESET
)

if choice.upper() == "OPEN":
    clear()

    divider()

    type_text("        ACCESSING PROJECT", CYAN, 0.06)

    divider()

    pause(0.7)

    type_text("> Verifying access...", GREEN)

    pause(0.7)

    type_text("> Access granted ✓", GREEN)

    pause(1)

    print()

    type_text("LEVEL 01", YELLOW)
    type_text("FIRST TRACE", CYAN)

    print()

    type_text("If you think you know", WHITE)
    type_text("where this started...", WHITE)

    print()

    type_text("Prove it. 👀", MAGENTA)

    pause(1)
# ==============================
# LEVEL 01 - QUESTION 01
# ==============================

while True:
    clear()

    print()
    type_text("╔══════════════════════════════════╗", CYAN)
    type_text("║          LEVEL 01                ║", CYAN)
    type_text("║          QUESTION 01             ║", CYAN)
    type_text("╚══════════════════════════════════╝", CYAN)

    print()

    type_text("Amar conversation start hua application khn hol?", MAGENTA)

    type_text("(What is the name of the application", WHITE)
    type_text("that started our first conversation?)", WHITE)

    print()

    type_text("A) Instagram 📸", GREEN)
    type_text("B) WhatsApp 💬", GREEN)
    type_text("C) Facebook 👀", GREEN)
    type_text("D) Telegram 😭", GREEN)

    print()

    answer = input(CYAN + "SELECT: " + RESET).strip().upper()

    if answer == "A":
        print()
        type_text("✓ ANSWER VERIFIED", GREEN)
        pause(1)
        break

    elif answer == "B":
        print()
        type_text("uff ki j hb tmr 😭😂", MAGENTA)
        type_text("correct answer diya na...", YELLOW)
        pause(1.5)

    elif answer == "C":
        print()
        type_text("Tmi FB use kora naki? 😂", MAGENTA)
        type_text("Jodi nokora... good girl 😌", YELLOW)
        type_text("Correct answer karone retry kora.", CYAN)
        pause(1.5)

    elif answer == "D":
        print()
        type_text("Tumi secret agent neki? 🕵️😂", MAGENTA)
        type_text("inbox choose krbo...", YELLOW)
        pause(1.5)

    else:
        print()
        type_text("Only A, B, C or D choose kora 😭", YELLOW)
        pause(1)
# ==============================
# LEVEL 01 - QUESTION 02
# ==============================

while True:
    clear()

    print()
    type_text("╔══════════════════════════════════╗", CYAN)
    type_text("║          LEVEL 01                ║", CYAN)
    type_text("║          QUESTION 02             ║", CYAN)
    type_text("╚══════════════════════════════════╝", CYAN)

    print()

    type_text("Eta date, jitu date mur karone eta date-e hoi...", MAGENTA)
    type_text("(A date, which is more than just a date for me...)", WHITE)

    print()

    type_text("19 + 08 + 2025 = ?", YELLOW)

    print()

    type_text("A) 2032 🤔", GREEN)
    type_text("B) 2042 😂", GREEN)
    type_text("C) 2052 👀", GREEN)
    type_text("D) 2062 😭", GREEN)

    print()

    answer = input(CYAN + "SELECT: " + RESET).strip().upper()

    if answer == "C":
        print()
        type_text("✓ ANSWER VERIFIED", GREEN)
        type_text("math jana mane... 👀", GREEN)
        pause(1.5)
        break

    elif answer == "A":
        print()
        type_text("2032? 😭", MAGENTA)
        type_text("Math eitu accept nokore 😂", YELLOW)
        pause(1.5)

    elif answer == "B":
        print()
        type_text("2042? Olop kom hoi gol 😂", MAGENTA)
        type_text("Again try kora...", YELLOW)
        pause(1.5)

    elif answer == "D":
        print()
        type_text("2062? Future pora ahila niki? 😂", MAGENTA)
        type_text("Aru eta try kora 👀", YELLOW)
        pause(1.5)

    else:
        print()
        type_text("A, B, C or D choose kora 😭", YELLOW)
        pause(1)
# ==============================
# LEVEL 01 - QUESTION 03
# ==============================

while True:
    clear()

    print()
    type_text("╔══════════════════════════════════╗", CYAN)
    type_text("║          LEVEL 01                ║", CYAN)
    type_text("║          QUESTION 03             ║", CYAN)
    type_text("╚══════════════════════════════════╝", CYAN)

    print()

    type_text("Aami sinaki hoisilu...", CYAN)
    type_text("(We got to know each other -)", WHITE)

    print()

    type_text("Kun date asil hei din tu?", YELLOW)
    type_text("(What was the date of that day?)", WHITE)

    print()

    type_text("A) 17 August 2025 🌱", GREEN)
    type_text("B) 19 August 2025 👀", GREEN)
    type_text("C) 21 August 2025 😂", GREEN)
    type_text("D) 25 August 2025 😭", GREEN)

    print()

    answer = input(CYAN + "SELECT: " + RESET).strip().upper()

    if answer == "B":
        print()
        type_text("✓ ANSWER VERIFIED", GREEN)
        type_text("Hmm.. bujisu , tumi guess korisa nh 👀✨", MAGENTA)
        pause(1.5)
        break

    elif answer == "A":
        print()
        type_text("17 August? Olop xoonkale hoi gol 😂", MAGENTA)
        type_text("Aru eta try kora...", YELLOW)
        pause(1.5)

    elif answer == "C":
        print()
        type_text("21 August? 😭", MAGENTA)
        type_text("Nope... date tu olop agote asil 👀", YELLOW)
        pause(1.5)

    elif answer == "D":
        print()
        type_text("25 August? Eitu tu besi late hoi gol 😂", MAGENTA)
        type_text("Memory tu aru olop search kora...", YELLOW)
        pause(1.5)

    else:
        print()
        type_text("A, B, C or D choose kora 😭", YELLOW)
        pause(1)
# ==============================
# LEVEL 01 - QUESTION 04
# ==============================

while True:
    clear()

    print()
    type_text("╔══════════════════════════════════╗", CYAN)
    type_text("║          LEVEL 01                ║", CYAN)
    type_text("║          QUESTION 04             ║", CYAN)
    type_text("╚══════════════════════════════════╝", CYAN)

    print()

    type_text("Next level-r karone ready asa ne?", MAGENTA)
    type_text("(Are you ready for the next level?)", WHITE)

    print()

    type_text("A) Asu 😌 — unlock kora, curiosity hoi ase 😂", GREEN)
    type_text("B) Umm... aasu 👀 — etiya suspense aru nokoriba", GREEN)
    type_text("C) Aasu ✨ — tumar logot next level-tu experience koribole ready 😌💫", GREEN)
    type_text("D) Hmm... aasu 😂 — sau software-tu ki surprise loi ahise", GREEN)

    print()

    answer = input(CYAN + "SELECT: " + RESET).strip().upper()

    if answer == "C":
        print()
        type_text("✓ ANSWER VERIFIED", GREEN)
        pause(0.7)

        print()
        type_text("> LEVEL 01 COMPLETE ✓", CYAN)
        type_text("> ALL TRACES VERIFIED", GREEN)
        type_text("> MEMORY LINK: ESTABLISHED", MAGENTA)

        print()
        type_text("████████████████████ 100%", GREEN)

        pause(1.5)

        print()
        type_text("LEVEL 02", CYAN, 0.08)
        type_text("LOCKED 🔒", RED, 0.08)

        break

    elif answer == "A":
        print()
        type_text("Ready toh asa... but answer tu olop different asil 😌😂", MAGENTA)
        type_text("Aru eta try kora 👀", YELLOW)
        pause(1.5)

    elif answer == "B":
        print()
        type_text("Umm... suspense bhal lage niki? 😂", MAGENTA)
        type_text("But olop confidence loi C try kora 😌", YELLOW)
        pause(1.5)

    elif answer == "D":
        print()
        type_text("Surprise definitely ase... but choice tu nohoi 😂", MAGENTA)
        type_text("Aru eta try kora 👀", YELLOW)
        pause(1.5)

    else:
        print()
        type_text("A, B, C or D choose kora 😭", YELLOW)
        pause(1)
# ==============================
# LEVEL 02 - UNLOCK
# ==============================

clear()

print()

divider()

type_text("        LEVEL 01 COMPLETE ✓", GREEN, 0.05)
type_text("        EMAN FAST TMI !! Lvl - 2 sua.", YELLOW, 0.05)

divider()

pause(1)

print()

type_text("> Searching deeper memory...", CYAN)
pause(0.7)

type_text("> New connection detected...", GREEN)
pause(0.7)

type_text("> LEVEL 02 ACCESS AVAILABLE", MAGENTA)
pause(1)

print()

type_text("LEVEL 02", CYAN, 0.1)
type_text("eyat sob note kori jaba , bcz last question tu e tmk puzzle kri dibou pare", YELLOW, 0.08)

print()

type_text("Level 01 was about how it started aru alp fun krne haa...", WHITE)
type_text("aitu lvl pr koribole maybe taan nohobou pare.", WHITE)

print()

type_text("Tmi Hosakoi Ready ? 👀", YELLOW)

input(
    "\n" + CYAN + "ENTER Press kora Contineu koribole..." + RESET
)

clear()

divider()

type_text("        LEVEL 02 UNLOCKED 🔓", GREEN, 0.06)

divider()

pause(1)

# ==============================
# LEVEL 02 - QUESTION 01
# ==============================

while True:
        clear()

        divider()

        type_text("        LEVEL 02 • QUESTION 01", CYAN, 0.05)

        divider()

        print()
        type_text("Q1. Aami sinaki ne ?", YELLOW, 0.05)
        type_text("(Do we know each other?)", WHITE, 0.04)

        print()
        type_text("A) UMM", GREEN, 0.05)
        type_text("B) Nohoi", GREEN, 0.05)

        print()

        answer = input("Your answer: ").strip().upper()

        if answer == "A":
            print()
            type_text(
                "Accha ji 😌🌱",
                GREEN,
                0.04
            )
            pause(2)
            break

        elif answer == "B":
            print()
            type_text(
                "One's legend Said : nohole porichoy hiyare sinaki janu kunu hb pare... 💫🌱 😁",
                CYAN,
                0.04
            )
            type_text("notice kori thaka sob, nxt step t lgibou pare , btw Alop smile r lgt play kora, muru vl lgib.", YELLOW, 0.05)
            pause(3)

        else:
            print()
            type_text(
                "A ne B choose koriba... 😭😂",
                RED,
                0.04
            )
            pause(2)
    # ==============================
    # LEVEL 02 - QUESTION 02
    # ==============================

while True:
        clear()

        divider()

        type_text("        LEVEL 02 • QUESTION 02", CYAN, 0.05)

        divider()

        print()
        type_text(
            "Lvl 2 r pa sob notice koriba, nohole continue koribo niwariba..",
            YELLOW,
            0.04
        )
        type_text("Btw etiya question tu hol...", WHITE, 0.04)

        print()
        type_text(
            "eta word ot jdi tumak describe koribo kou kuntu option choose koriba...",
            YELLOW,
            0.04
        )
        type_text(
            "correct option tu he choose koriba..",
            CYAN,
            0.04
        )
        type_text("vbi lua? 👀🌱", GREEN, 0.05)

        print()
        type_text("A) pgl", YELLOW, 0.05)
        type_text("B) mentel", YELLOW, 0.05)
        type_text("C) eta option u choose nokoru", YELLOW, 0.05)
        type_text("D) next question", YELLOW, 0.05)

        print()

        answer = input("Your answer: ").strip().upper()

        if answer == "A":
            print()
            type_text(
                "tmi pgl nohoi , tmi queen hoi queen🌱",
                GREEN,
                0.05
            )
            pause(2)
            break

        elif answer == "B":
            print()
            type_text(
                "tmi nijk mentel buli describe koriba nki😂",
                CYAN,
                0.05
            )
            pause(2)

        elif answer == "C":
            print()
            type_text(
                "Kora sun, parba kunuba eta correct hoi 🤦🤦",
                YELLOW,
                0.05
            )
            pause(2)

        elif answer == "D":
            print()
            type_text(
                "nah , nxt question r karone ei question tur answer diboi lgibo",
                YELLOW,
                0.05
            )
            pause(3)

        else:
            print()
            type_text(
                "A, B, C, D... eta choose koriba! 😭😂",
                RED,
                0.04
            )
            pause(2)
    # ==============================
    # LEVEL 02 - QUESTION 03
    # ==============================

while True:
        clear()

        divider()

        type_text("        LEVEL 02 • QUESTION 03", CYAN, 0.05)

        divider()

        print()
        type_text(
            "words are not enough for the question <smiling enoji>...",
            YELLOW,
            0.04
        )
        type_text(
            "question tu loding hoi ase roba.",
            WHITE,
            0.04
        )
        type_text(
            "same question hoi agr tu nisina , nijk eta word t describe kora? 👀🌱",
            YELLOW,
            0.05
        )

        print()
        type_text("A) Pagol 😂🐷", GREEN, 0.05)
        type_text("B) Interesting 🌱🐷", CYAN, 0.05)
        type_text("C) Good Girl 🐷🌱", YELLOW, 0.05)
        type_text("D) Eitu question-e cancel kori diya 😂🚪", MAGENTA, 0.05)

        print()

        answer = input("d ").strip().upper()

        if answer == "A":
            print()
            type_text(
                "blck kri diba j akou , hykrne xunkal krisu , 🐷",
                GREEN,
                0.05
            )
            pause(2)
            break

        elif answer == "B":
            print()
            type_text(
                "Interesting buli nijokei certificate di dila ne 😭😂🌱",
                CYAN,
                0.05
            )
            pause(2)

        elif answer == "C":
            print()
            type_text(
                "tmi queen hoi queen kintu correct option eitu noohoi 😭😂🐷🌱",
                YELLOW,
                0.05
            )
            pause(2)

        elif answer == "D":
            print()
            type_text(
                "Question cancel kori dilei nohoi... notice tu already hoi gol 😭😂",
                MAGENTA,
                0.05
            )
            pause(3)

        else:
            print()
            type_text(
                "A, B, C, D... eta choose koriba! 😭😂",
                RED,
                0.04
            )
            pause(2)

    # ==============================
    # LEVEL 02 - QUESTION 04
    # ==============================

while True:
        clear()

        divider()

        type_text("        LEVEL 02 • QUESTION 03", CYAN, 0.05)

        divider()

        print()
        type_text(
            "starting hoisil he, tmi xunkal korila",
            YELLOW,
            0.04
        )
        type_text(
            "btw emanote xekh koru main concept aru nxt lvl nxt step nai eyate khtm hb 0are  tu...",
            WHITE,
            0.04
        )
        type_text(
            "flirty type lgisil nki , jdi lgisil , jdi lgisil lvl 2 hard kribor krne krisilu , qi quesrion tu  , question bonabou time nai .  kiba eta option choose krilei maybe finish hoi jqbo , ba nohobou pare , 👀🌱",
            CYAN,
            0.05
        )

        print()
        type_text("A) A", GREEN, 0.05)
        type_text("B) B", CYAN, 0.05)
        type_text("C) C", YELLOW, 0.05)
        type_text("D) option nai , Ansewr u nai , finshing tu faltu kri disu, time ni , tmi blck kri diba j🚪", GREEN, 0.05)

        print()

        answer = input("Your answer: ").strip().upper()

        if answer == "A":
            print()
            type_text(
                "THNQ OPEN KORA KRNE",
                GREEN,
                0.05
            )
            pause(2)
            break

        elif answer == "B":
            print()
            type_text(
                "THNQ ISTALL KORA KRNE🌱",
                CYAN,
                0.05
            )
            pause(2)

        elif answer == "C":
            print()
            type_text(
                "goood ending dibole time nai 😭🌱",
                YELLOW,
                0.05
            )
            pause(2)

        elif answer == "D":
            print()
            type_text(
                "block krim koisila nh, hykrne final view sabo nidiu 😭",
                MAGENTA,
                0.05
            )
            pause(3)

        else:
            print()
            type_text(
                "A, B, C, D... eta choose koriba! 😭😂",
                RED,
                0.04
            )
            pause(2)
# ==============================
# LEVEL 02 — FINAL ENDING
# ==============================

os.system("clear")

type_text("\n⚠️ SYSTEM GLITCH DETECTED...", RED, 0.04)
time.sleep(0.8)

type_text("▓▒░ CONNECTION UNSTABLE ░▒▓", YELLOW, 0.04)
time.sleep(0.7)

type_text("\n...reconnecting...", CYAN, 0.06)
time.sleep(1)

os.system("clear")

type_text("╔══════════════════════════════════╗", CYAN, 0.02)
type_text("║          SYSTEM COMPLETE         ║", CYAN, 0.02)
type_text("╚══════════════════════════════════╝", CYAN, 0.02)

time.sleep(0.8)

type_text("\n XEKH KORI DILU EMANOTE , THNQ OPEN KORA KRNE ... 🌱✨", GREEN, 0.05)
time.sleep(0.6)

type_text(
    "\nAru open korila jodi, ei code tu send koriba muk —",
    WHITE,
    0.04
)

type_text("\n              XR333", YELLOW, 0.12)

time.sleep(0.5)

type_text(
    "\n\n(Ei code tu dile he moi gom paam tumi open korisa buli , ARU HOSAKOI JODI ALOP VAL LGILE THEN "333" SEND KORIBA😁🌱)",
    CYAN,
    0.035
)

time.sleep(1.5)

type_text("\n\n▓▓▓ SESSION TERMINATED ▓▓▓", RED, 0.04)

input("\n\nPress ENTER to exit...")
