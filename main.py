import pandas as pd

try:
    # Load files
    raw_df = pd.read_csv("raw_data.csv")
    reference_df = pd.read_excel("reference_data.xlsx")

    # Clean column names
    raw_df.columns = raw_df.columns.str.strip()
    reference_df.columns = reference_df.columns.str.strip()

    # Correct column names (based on your file)
    raw_key_column = "lookup_key"
    reference_lookup_column = "lookup_key"

    # Remove duplicates from raw
    raw_df = raw_df[[raw_key_column]].dropna().drop_duplicates()

    # Perform inner join
    mapped_df = pd.merge(
        raw_df,
        reference_df,
        left_on=raw_key_column,
        right_on=reference_lookup_column,
        how="inner"
    )

    # Save output
    mapped_df.to_csv("mapped_output.csv", index=False)

    print(" Mapping completed successfully!")
    print("Total matched rows:", len(mapped_df))

except Exception as e:
    print(" Error occurred:", e)