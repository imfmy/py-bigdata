scores = {"a": 1, "b": 2, "c": 3, "d": 2, "z": 1, "y": 3}
highest_score = max(scores.values())
print(highest_score)
highest_score_names = [name for name, score in scores.items() if score == highest_score]

print("分数最高的名字是:", highest_score_names)
