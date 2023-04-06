import pandas as pd
import numpy as np

from scipy.stats import norm, chi2


chat_id = 32412687 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    s2 = np.sum(np.square(x))
    left = s2 / chi2.ppf(1 - alpha / 2, 2 * len(x))
    right = s2 / chi2.ppf(alpha / 2, 2 * len(x))
    left = np.sqrt(left / 43)
    right = np.sqrt(right / 43)
    if right < left:
        left, right = right, left
    return left, right
