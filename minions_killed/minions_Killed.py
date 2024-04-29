import matplotlib.pyplot as plt


def minions_Killed(df):
    minions_killed = df['minions_killed']

    x_axis1 = minions_killed.value_counts().index.tolist()
    y_axis1 = minions_killed.value_counts().values.tolist()

    plt.bar(x_axis1, y_axis1)
    plt.title('Frequency of Minions Killed')
    plt.xlabel('Many or Few')
    plt.ylabel('Frequency')
    plt.grid(axis='y')
    plt.savefig('minions_Killed.png')
    plt.close()
