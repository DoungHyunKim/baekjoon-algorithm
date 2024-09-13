A, B, V = map(int, input().split())

# 하루에 A만큼 올라가고, 밤에 B만큼 미끄러짐
# 마지막 날은 미끄러지지 않으므로, 이를 고려하여 계산

# (V - A)만큼 올라간 뒤에, 매일 (A - B)만큼 올라감
count = (V - B - 1) // (A - B) + 1

print(count)
