import daft

df = daft.read_parquet("data/yellow_tripdata_2023-12.parquet")
print(df.show())
