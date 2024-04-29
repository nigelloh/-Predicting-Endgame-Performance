import matplotlib.pyplot as plt


def champion_Selection(df):
    # get top 10 and bottom 10 most frequent champions
    n = 10
    df['champion'].value_counts()[:n]
    x_axis = []
    top_10 = df['champion'].value_counts().nlargest(n).index.tolist()
    bottom_10 = df['champion'].value_counts().nsmallest(n).sort_values(ascending = False).index.tolist()
    x_axis = top_10 + bottom_10

    y_axis = []
    for i in x_axis:
        count = 0
        for j in df['champion']:
            if i in j:
                count += 1 
        y_axis.append(count)

    # Plotting of 
    plt.bar(x_axis, y_axis)
    plt.title("Frequency of Highest 10 and Lowest 10 Champions Used")
    plt.xlabel("Champions")
    plt.ylabel("Frequency of Champions Used")
    plt.xticks(fontsize=6.5, rotation=90)
    plt.subplots_adjust(bottom=0.25)
    plt.grid(axis='y')
    plt.savefig("champion_Selection.png")
    plt.close()

