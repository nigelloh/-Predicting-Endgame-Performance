from feature_selection import *
from gold_Earned import *
from champion_Selection import *
from minions_Killed import *
from linearReg1 import *
from linearReg2 import *
from linearRegTest import *
from decision_tree import *
import pandas as pd


def main():
    merged = pd.read_csv('merged.csv')
    training = pd.read_csv('training.csv')
    testing = pd.read_csv('testing.csv')

    champion_Selection(merged)
    minions_Killed(merged)
    gold_Earned(merged)
    linear_reg_features = feature_selection_regression(merged)
    decision_tree_features = feature_selection_decision_tree(merged)
    linearReg1(training, linear_reg_features)
    linearReg2(training, linear_reg_features)
    linearRegTest(training, testing, linear_reg_features)
    decision_tree(training, testing, decision_tree_features)

# Data Processing is fun!!!
main()

