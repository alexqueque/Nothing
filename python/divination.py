import random
import pandas as pd

# 随机生成上卦、下卦、动爻
upper = random.randint(1, 8)
lower = random.randint(1, 8)
change = random.randint(1, 6)

# 八卦名称
bagua = {
    1: '乾', 2: '兑', 3: '离', 4: '震',
    5: '巽', 6: '坎', 7: '艮', 8: '坤'
}

print(f"上卦: {bagua[upper]} ({upper})")
print(f"下卦: {bagua[lower]} ({lower})")
print(f"动爻: 第{change}爻")

# 读取数据
hexagrams_df = pd.read_csv('/Users/qq/Nothing/data/hexagrams_data.csv')
gua_link_df = pd.read_csv('/Users/qq/Nothing/data/gua_link.csv')

# 查询卦象(字段名: lower_trigram)
row = hexagrams_df[(hexagrams_df['upper_number'] == upper) & (hexagrams_df['lower_trigram'] == lower)]
if not row.empty:
    row = row.iloc[0]
    print(f"\n卦名: {row['hexagram_name']}")
    print(f"卦象: {row['hexagram_image']}")
    print(f"卦义: {row['hexagram_meaning']}")

    # 查询动爻
    change_row = gua_link_df[(gua_link_df['gui-name'] == row['hexagram_name']) & (gua_link_df['number3'] == change)]
    if not change_row.empty:
        print(f"动爻名称: {change_row.iloc[0]['change-number']}")

    print(f"\n周易原文: {row['zhou_url']}")
    print(f"高岛易断: {row['gao_url']}")
else:
    print("未找到对应卦象数据")
