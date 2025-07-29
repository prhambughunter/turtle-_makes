import turtle
import time

# لیست سوال‌ها و جواب‌ها


# تنظیمات لاک‌پشت
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.goto(-200, 0)
player.pendown()

# تابع نمایش پیام
def ask_question(question, correct_answer):
    answer = turtle.textinput("سؤال", question)
    return answer == correct_answer

# اجرای مسابقه
for question, answer in questions:
    player.forward(100)
    time.sleep(0.5)
    correct = ask_question(question, answer)
    if not correct:
        turtle.write("پاسخ اشتباه بود! بازی تمام شد.", font=("Arial", 14, "bold"))
        break
else:
    turtle.write("آفرین! همه سوالات رو درست جواب دادی! 🎉", font=("Arial", 14, "bold"))

turtle.done()
