"""
remove_red_digits_bbox.py
Удаляет красный телефон-водяной знак.
Ищем красные пиксели  ⇒  находим контуры  ⇒  оставляем
только узкие длинные прямоугольники  ⇒  inpaint.

💡  Звук не трогаем.
"""

import cv2
import numpy as np
from tqdm import tqdm
from pathlib import Path

# ────────── файлы ──────────
SRC_VIDEO = Path("IMG_6488.MP4")
OUT_VIDEO = Path("clean_no_audio.mp4")

# ────────── HSV красного ──────────
LOW1 = np.array([0,   90, 100], dtype=np.uint8)
UP1  = np.array([10, 255, 255], dtype=np.uint8)
LOW2 = np.array([170, 90, 100], dtype=np.uint8)
UP2  = np.array([180, 255, 255], dtype=np.uint8)

# ────────── геометрический фильтр ──────────
MIN_AREA = 400       # минимальная площадь контура
MAX_AREA = 15000     # максимальная (чтобы не хватать большие объекты)
MIN_RATIO = 3.0      # ширина / высота
MAX_RATIO = 20.0     # запас

# ────────── морфология + inpaint ──────────
KERNEL = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
DILATE_ITER = 2       # расширяем маску
INPAINT_RAD = 3       # радиус Telea

# ────────── проверки ──────────
assert SRC_VIDEO.exists(), "Исходный файл не найден"

# ────────── потоки ──────────
cap   = cv2.VideoCapture(str(SRC_VIDEO))
fps   = cap.get(cv2.CAP_PROP_FPS)
w     = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h     = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
four  = cv2.VideoWriter_fourcc(*"mp4v")
out   = cv2.VideoWriter(str(OUT_VIDEO), four, fps, (w, h))

# ────────── обработка ──────────
for _ in tqdm(range(total), desc="Чистим"):
    ok, frame = cap.read()
    if not ok:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.bitwise_or(cv2.inRange(hsv, LOW1, UP1),
                          cv2.inRange(hsv, LOW2, UP2))

    # шум —> морфология
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, KERNEL)
    for _ in range(DILATE_ITER):
        mask = cv2.dilate(mask, KERNEL)

    # ---------- фильтруем контуры ----------
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)
    clean_mask = np.zeros_like(mask)

    for cnt in contours:
        x, y, w_box, h_box = cv2.boundingRect(cnt)
        area   = w_box * h_box
        ratio  = w_box / h_box if h_box else 0

        if (MIN_AREA <= area <= MAX_AREA and
            MIN_RATIO <= ratio <= MAX_RATIO):
            # это похоже на «строчку цифр» — добавляем в маску
            cv2.rectangle(clean_mask, (x, y),
                          (x + w_box, y + h_box), 255, -1)

    # если ничего не найдено — пишем кадр как есть
    if clean_mask.mean() < 1:
        out.write(frame)
        continue

    cleaned = cv2.inpaint(frame, clean_mask,
                          INPAINT_RAD, cv2.INPAINT_TELEA)
    out.write(cleaned)

cap.release()
out.release()
print("Готово:", OUT_VIDEO)
