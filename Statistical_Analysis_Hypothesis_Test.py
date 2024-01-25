#import pandas package

import pandas as pd # data  loading, manipulation and wrangling
pd.set_option('display.max_rows', None) # display all rows in the dataset
pd.set_option('display.max_columns', None) # display all columns in the dataset
pd.set_option('display.float_format', lambda x: '%.2f' % x) # suppress all scientific notations and round to 2 decimal places
import numpy as np

#Visualization
import plotly.express as px #interactive visualization
import seaborn as sns # statistical visualization
import matplotlib.pyplot as plt # basic visualization
# Command to tell Python to actually display the graphs
%matplotlib inline

# statistical Analysis library
import scipy.stats as stats
from scipy.stats import ttest_ind
from scipy.stats import shapiro

#connecting to google drive
from google.colab import drive
drive.mount('/content/drive')

#read data from google drive
travelinsurance = pd.read_csv('/content/drive/MyDrive/wale/datasets/travel_insurance.csv')
df = travelinsurance.copy()
df.head(10)
df.info()

# for categorical/Non-numeric variables
df.describe(include= 'object').T

# for continuous/numeric variables

df.describe(include = ['int','float']).T
list(df.columns)

df.columns = df.columns.str.replace('(','_')
df.columns = df.columns.str.replace(')','')
# replace all white spaces and special characters with _
df.columns = df.columns.str.replace(' ', '_')
df.columns = df.columns.str.replace('__','_')
list(df.columns)

#df.columns = df.columns.str.replace('','_')
list(df.columns)

#Convert all records in Location from uppercase to lowercase (while capitlaizing the first Letter of each country) for example : FRANCE to France


df['Location']= df.Location.str.title()
df['Location'].value_counts()

df['Net_Sales'].head(5)
df['Net_Sales'].abs().head(5)

# function to create labeled barplots


def labeled_barplot(data, feature, perc=False, n=None):
    """
    Barplot with percentage at the top

    data: dataframe
    feature: dataframe column
    perc: whether to display percentages instead of count (default is False)
    n: displays the top n category levels (default is None, i.e., display all levels)
    """

    total = len(data[feature])  # length of the column
    count = data[feature].nunique()
    if n is None:
        plt.figure(figsize=(count + 1, 5))
    else:
        plt.figure(figsize=(n + 1, 5))

    plt.xticks(rotation=90, fontsize=15)
    ax = sns.countplot(
        data=data,
        x=feature,
        palette="Paired",
        order=data[feature].value_counts().index[:n].sort_values(),
    )

    for p in ax.patches:
        if perc == True:
            label = "{:.1f}%".format(
                100 * p.get_height() / total
            )  # percentage of each class of the category
        else:
            label = p.get_height()  # count of each level of the category

        x = p.get_x() + p.get_width() / 2  # width of the plot
        y = p.get_height()  # height of the plot

        ax.annotate(
            label,
            (x, y),
            ha="center",
            va="center",
            size=12,
            xytext=(0, 5),
            textcoords="offset points",
        )  # annotate the percentage

    plt.show()  # show the plot

labeled_barplot(df,'Product_Name',perc = True)

labeled_barplot(df,"Distribution_Channel", perc=True)
labeled_barplot(df,"Agency_Type", perc=True)
labeled_barplot(df,"Claim", perc=True)
for col in df[['Agency_Type','Claim','Product_Name','Distribution_Channel']].columns:
    labeled_barplot(df, col)

# function to plot a boxplot and a histogram along the same scale.


def histogram_boxplot(data, feature, figsize=(12, 7), kde=False, bins=None):
    """
    Boxplot and histogram combined

    data: dataframe
    feature: dataframe column
    figsize: size of figure (default (12,7))
    kde: whether to the show density curve (default False)
    bins: number of bins for histogram (default None)
    """
    f2, (ax_box2, ax_hist2) = plt.subplots(
        nrows=2,  # Number of rows of the subplot grid= 2
        sharex=True,  # x-axis will be shared among all subplots
        gridspec_kw={"height_ratios": (0.25, 0.75)},
        figsize=figsize,
    )  # creating the 2 subplots
    sns.boxplot(
        data=data, x=feature, ax=ax_box2, showmeans=True, color="violet"
    )  # boxplot will be created and a star will indicate the mean value of the column
    sns.histplot(
        data=data, x=feature, kde=kde, ax=ax_hist2, bins=bins, palette="winter"
    ) if bins else sns.histplot(
        data=data, x=feature, kde=kde, ax=ax_hist2
    )  # For histogram
    ax_hist2.axvline(
        data[feature].mean(), color="green", linestyle="--"
    )  # Add mean to the histogram
    ax_hist2.axvline(
        data[feature].median(), color="black", linestyle="-"
    )  # Add median to the histogram

for col in df[['Age','Net_Sales','Duration','Commision_in_value']].columns:
    histogram_boxplot(df, col)

def stacked_barplot(data, predictor, target):
    """
    Print the category counts and plot a stacked bar chart

    data: dataframe
    predictor: independent variable
    target: target variable
    """
    count = data[predictor].nunique()
    sorter = data[target].value_counts().index[-1]
    tab1 = pd.crosstab(data[predictor], data[target], margins=True).sort_values(
        by=sorter, ascending=False
    )
    print(tab1)
    print("-" * 120)
    tab = pd.crosstab(data[predictor], data[target], normalize="index").sort_values(
        by=sorter, ascending=False
    )
    tab.plot(kind="bar", stacked=True, figsize=(count + 1, 5))
    plt.legend(
        loc="lower left",
        frameon=False,
    )
    plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
    plt.show()

stacked_barplot(df,"Commision_in_value","Agency_Type")

#Top 5 countries with the highest net sales - Singapore, UnitedStates, Australia,China, Thailand
most_least_commission = df.groupby('Agency').sum()[['Commision_in_value']].sort_values('Commision_in_value',ascending = False)
most_least_commission

product_least_duration = df.groupby('Product_Name').sum()[['Duration']].sort_values('Duration',ascending = False).tail(2)
product_least_duration

countries_avghighest_netsales = df.groupby('Location').mean()[['Net_Sales']].sort_values('Net_Sales',ascending = False).head(5)
countries_avghighest_netsales

# select the relevant columns - Net_Sales and Location

df1 = df[["Net_Sales","Location"]]

#
cols = df1.columns.difference(['Location'])

# step 3: filter for the countries - France and Germany

group1 = df1[df1['Location']=='Germany']
group2 = df1[df1['Location']=='France']

# Run a Mann whitney since we have two groups

out = pd.DataFrame(stats.mannwhitneyu(group1[cols], group2[cols]),
                   columns=cols, index=['statistic', 'pvalue'])

out


# select the relevant columns - Net_Sales and Location

df1 = df[["Commision_in_value","Location"]]

#
cols = df1.columns.difference(['Location'])

# step 3: filter for the countries - France and Germany

group1 = df1[df1['Location']=='China']
group2 = df1[df1['Location']=='India']
#group3 = df1[df1['Location']=='Spain']

# Run a Mann whitney since we have two groups

out = pd.DataFrame(stats.mannwhitneyu(group1[cols], group2[cols]),#group3[cols]),
                   columns=cols, index=['statistic', 'pvalue'])

out

