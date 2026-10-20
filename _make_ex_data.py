"""Готовые примеры для studio.html и school.html (d/exstudio.json, d/exschool.json)."""
import json
from pathlib import Path

D = Path(__file__).resolve().parent / "d"
PAL = [("#2B1F1D", "#F3E6E3"), ("#9C4E57", "#FBEDEE"), ("#B98A5E", "#FFF6EC"), ("#3F5A4C", "#EAF2EC"),
       ("#34465E", "#E8EEF6"), ("#6B4E7A", "#F2ECF6")]


def svc(items):
    out = []
    for i, (name, price, frm, dur, cat) in enumerate(items):
        tb, tc = PAL[i % len(PAL)]
        out.append({"name": name, "price": price, "from": frm, "dur": dur, "cat": cat, "tb": tb, "tc": tc, "id": f"s{i}"})
    return out


studio = {"kind": "booking", "name": "Студия танца «Ритм»", "sub": "танцы и фитнес · запись на пробное",
          "tagline": "Первое занятие — за полцены.", "channel": "", "manager": "@ritm_dance", "ns": "",
          "cats": ["Танцы", "Дети", "Фитнес"],
          "services": svc([("Пробное: Jazz-funk", 500, False, "1 ч", "Танцы"),
                           ("Пробное: High heels", 500, False, "1 ч", "Танцы"),
                           ("Абонемент на 8 занятий", 4200, False, "1 месяц", "Танцы"),
                           ("Детская группа 6–9 лет", 3800, False, "8 занятий", "Дети"),
                           ("Растяжка", 450, False, "1 ч", "Фитнес"),
                           ("Пилатес", 450, False, "55 мин", "Фитнес")])}
school = {"kind": "booking", "name": "Школа английского «Point»", "sub": "курсы для детей и взрослых · пробный урок",
          "tagline": "Первый урок — бесплатно.", "channel": "", "manager": "@point_school", "ns": "",
          "cats": ["Взрослые", "Дети", "Индивидуально"],
          "services": svc([("Курс A1 с нуля", 12900, False, "3 месяца", "Взрослые"),
                           ("Пробный урок", 0, False, "45 мин", "Взрослые"),
                           ("Разговорный клуб", 700, False, "1 ч", "Взрослые"),
                           ("Английский для детей 7–10 лет", 4800, False, "8 уроков", "Дети"),
                           ("Подготовка к ОГЭ", 5600, False, "8 уроков", "Дети"),
                           ("Индивидуально с преподавателем", 1500, True, "1 ч", "Индивидуально")])}
for name, data in (("exstudio", studio), ("exschool", school)):
    (D / f"{name}.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print("ok", name)
