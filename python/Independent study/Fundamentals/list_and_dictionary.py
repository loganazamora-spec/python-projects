data = [{"age": 25, "score": 88}, 
        {"age": 30, "score": 92}, 
        {"age": 22, "score": 79}]

total_score = sum(row["score"] for row in data)

avg_score = total_score / len(data)
