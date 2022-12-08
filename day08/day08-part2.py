import pandas as pd


def build_dataframe(data_file: str) -> pd.DataFrame:

    # Create dataframe and convert all valuse to string
    temp_df = pd.read_table(data_file, header=None)
    temp_df = temp_df.astype(str)

    # Split string values into discrete columns and reset column index
    df = temp_df[0].str.split("", n=temp_df.shape[0], expand=True)
    df.drop(df.columns[0], axis=1, inplace=True)
    df.columns = range(df.shape[1])

    # Convert all valuse back to integers
    df = df.astype(int)

    return df


def find_visibility(slice: list, tree_value: int):
    visibility = 0

    if len(slice) == 1:
        visibility = 1
    elif len(slice) > 1:
        for i in slice:
            if i < tree_value:
                visibility += 1
            elif i >= tree_value:
                visibility += 1
                break
    return visibility


def main(data_file: str) -> None:

    df = build_dataframe(data_file)

    top_tree_score: int = 0

    for index, row in df.iterrows():
        # Skip the first and last rows.  Those trees scores will always be 0.
        if (index == 0) or (index == df.shape[1] - 1):
            continue

        curr_row = df.loc[index, :].values.flatten().tolist()

        for i, tree in enumerate(curr_row):

            left_slice = curr_row[:i]
            left_slice.reverse()
            trees_left = find_visibility(left_slice, tree)

            right_slice = curr_row[i + 1 :]
            trees_right = find_visibility(right_slice, tree)

            curr_col = df.loc[:, i].values.flatten().tolist()

            top_slice = curr_col[0:index]
            top_slice.reverse()
            trees_top = find_visibility(top_slice, tree)

            bottom_slice = curr_col[index + 1 :]
            trees_bottom = find_visibility(bottom_slice, tree)

            scenic_score = trees_right * trees_left * trees_top * trees_bottom

            if scenic_score > top_tree_score:
                top_tree_score = scenic_score

    print(f"Top Tree Score = {top_tree_score}")  # correct answer is 590824


if __name__ == "__main__":
    main("data/input.txt")
