from sklearn.feature_selection import mutual_info_classif
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt


def feature_selection_regression(data):
    print("\n===Regression Feature Selection===")
    filtered_features = []
    feature_mi = {}
    THRESHOLD = 0.4
    features = data[['damage_objectives', 'damage_building', 'damage_turrets', 'kda', 'turret_kills', 'vision_score', 'damage_total']]
    class_label = data['gold_earned']
    mi_arr = mutual_info_classif(X=features, y=class_label)
    for feature, mi in zip(features.columns, mi_arr):
        feature_mi[feature] = mi
        if (mi >= THRESHOLD):
            filtered_features.append(feature)

    plt.bar(range(len(feature_mi)), sorted(feature_mi.values()), align='center')
    plt.xticks(range(len(feature_mi)), list(feature_mi.keys()), fontsize=6.5, rotation='vertical')
    plt.subplots_adjust(bottom=0.25)
    plt.grid(axis='y')
    plt.xlabel("Features")
    plt.ylabel("Mutual Information Score (MI)")
    plt.title('Mutual Information of Features for Class: \'gold_earned\'')
    plt.savefig("feature_selection_mi")
    plt.close()

    print("Done!")

    return filtered_features


def feature_selection_decision_tree(data):
    print("\n===Decision Tree Feature Selection===")
    ALPHA = 0.05
    features = data[['role', 'champion']]
    class_label = data['minions_killed']

    filtered_features = []
    for feature in ('role', 'champion'):
        cont_table = pd.crosstab(class_label, features[feature])
        chi2_val, p, dof, expected = stats.chi2_contingency(cont_table.values, correction=False)

        if (p < ALPHA):
            filtered_features.append(feature)

    print("Done!")

    return filtered_features

