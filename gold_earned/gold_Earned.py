import matplotlib.pyplot as plt


def gold_Earned(df):
    goldEarned = df['gold_earned']
    plt.hist(goldEarned, bins = 100)
    plt.xlabel('Gold Earned')
    plt.ylabel('Frequency of Amount Gold Earned')
    plt.title('Gold Earned')
    plt.grid()
    plt.savefig('gold_Earned.png')
    plt.close()
