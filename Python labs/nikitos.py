news_paper = set(input("Введите текст газеты: ").lower().split())
paper = set(input("Введите текст записки о выкупе: ").lower().split())
print("Из газеты можно составить записку." if paper <= news_paper else "Из газеты нельзя составить записку.")
