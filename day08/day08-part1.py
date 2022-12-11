"""This is a hot mess of linear, nested, redundant code, but it gets the job done.
Part two was done a lot cleaner.

Other code I looked at after my attempt: 
https://github.com/benji-york/advent-of-code-2022/tree/main/8

Useful tips to do this with less code and it runs faster.
"""

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


def main(data_file: str) -> None:

    df = build_dataframe(data_file)

    # Calculate the number of visible trees on the peremiter.
    visible_cnt: int = df.shape[0] * 2 + (df.shape[1] - 2) * 2

    for index, row in df.iterrows():
        # Skip the first and last rows.  Those trees are visible and already counted.
        if (index == 0) or (index == df.shape[1] - 1):
            continue

        curr_row = df.loc[index, :].values.flatten().tolist()

        visible_left: bool = False
        visible_right: bool = False
        visible_up: bool = False
        visible_down: bool = False
        # iterate through middle values
        for i in range(1, len(curr_row) - 1):
            # compare to list values to the left of current postion
            left_slice = list(set(curr_row[0:i]))
            left_slice.sort()
            for j, value in enumerate(left_slice):
                if value < curr_row[i]:
                    visible_left = True
                else:
                    visible_left = False

            if visible_left:
                visible_cnt += 1
            else:
                # compare to list values to the right of current position
                # no need to do this if we know it is already visible from the left
                right_slice = list(set(curr_row[i + 1 :]))
                right_slice.sort()
                for j, value in enumerate(right_slice):
                    if value < curr_row[i]:
                        visible_right = True
                    else:
                        visible_right = False

                if visible_right:
                    visible_cnt += 1
                else:
                    # compare to list values above the current position
                    # no need to do this if we know it is already visible from the left or right
                    curr_col = df.loc[:, i].values.flatten().tolist()
                    # compare to list values to the left/above of current postion
                    up_slice = list(set(curr_col[0:index]))
                    up_slice.sort()
                    for j, value in enumerate(up_slice):
                        if value < curr_col[index]:
                            visible_up = True
                        else:
                            visible_up = False
                    if visible_up:
                        visible_cnt += 1
                    else:
                        # compare to list values below the current position
                        # no need to do this if we know it is already visible from the left or right or above
                        curr_col = df.loc[:, i].values.flatten().tolist()
                        # compare to list values to the right/below of current postion
                        down_slice = list(set(curr_col[index + 1 :]))
                        down_slice.sort()
                        for j, value in enumerate(down_slice):
                            if value < curr_col[index]:
                                visible_down = True
                            else:
                                visible_down = False
                        if visible_down:
                            visible_cnt += 1

    print(f"Total visible count = {visible_cnt}")  # 1719 is the correct answer


if __name__ == "__main__":
    main("data/input.txt")
