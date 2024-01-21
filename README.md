# Hypothesis-Test
Objective:
To test various hypothesis relating to Travel insurance data
Data Processing Task

For each column name, replace all white spaces and special characters with _

-- for example: Distribution Channel to Distribution_Channel

Convert all records in Location from uppercase to lowercase (while capitlaizing the first Letter of each country)

-- for example : FRANCE to France

Convert column with negative values to absolute values
-- for example : -49 to 49

Map countries in Location to their corresponding continent and store in another column named Continent

-- for example : France --> Europe

Basic Questions:

Visualize the distribution of Distribution_Channel,Agency_Type, Continent.

visualize the relationship between continent and Net_sales

visualize the relationship between Agency_Type and Commission

Key business questions

What agency has the most and least commission?
What Product has the least Duration?
Top 5 countries with the highest net sales
There's no significant differences between the net sales of France and Germany, can you test this hypothesis?
Is there a statistical difference in the average age of insurees of China and India?
looking across all continents - is there statistical difference between commision received by travel agents ? if yes, where are the differences?
look into

shapiro test https://www.statology.org/shapiro-wilk-test-python/,

t-test https://www.statology.org/pandas-t-test/

Mann whitney test https://www.statology.org/mann-whitney-u-test-python/

look into :

https://www.statology.org/kruskal-wallis-test-python/

https://www.statology.org/one-way-anova-python/

https://www.statology.org/tukey-test-python/

Dataset:
Claim: Claim (Yes or No)

Name of agency (Agency)

Type of travel insurance agencies (Agency Type)

Distribution channel of travel insurance agencies (Distribution.Channel)

Name of the travel insurance products (Product.Name)

Duration of travel (Duration)

Destination of travel (Destination)

Amount of sales of travel insurance policies (Net.Sales)

Commission received for travel insurance agency (Commission)

Age of insured (Age)
