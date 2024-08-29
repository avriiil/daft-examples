import daft

# Create a dataframe with a column "a" that has values [1, 2, 3]
df = daft.from_pydict({"a": [1, 2, 3]})

# Create new columns called "a_plus_1" and "a_startswith_1" using Expressions
df = df.select(
    col("a"),
    (col("a") + 1).alias("a_plus_1"),
    col("a").cast(DataType.string()).str.startswith("1").alias("a_startswith_1"),
)

print(df.show())
