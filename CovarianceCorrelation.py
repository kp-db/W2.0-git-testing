# Databricks notebook source
# MAGIC %md # Covariance and Correlation

# COMMAND ----------

# MAGIC %md Covariance measures how two variables vary in tandem from their means.
# MAGIC 
# MAGIC For example, let's say we work for an e-commerce company, and they are interested in finding a correlation between page speed (how fast each web page renders for a customer) and how much a customer spends.
# MAGIC 
# MAGIC numpy offers covariance methods, but we'll do it the "hard way" to show what happens under the hood. Basically we treat each variable as a vector of deviations from the mean, and compute the "dot product" of both vectors. Geometrically this can be thought of as the angle between the two vectors in a high-dimensional space, but you can just think of it as a measure of similarity between the two variables.
# MAGIC 
# MAGIC First, let's just make page speed and purchase amount totally random and independent of each other; a very small covariance will result as there is no real correlation:

# COMMAND ----------

# MAGIC %matplotlib inline
# MAGIC 
# MAGIC import numpy as np
# MAGIC from pylab import *
# MAGIC 
# MAGIC def de_mean(x):
# MAGIC     xmean = mean(x)
# MAGIC     return [xi - xmean for xi in x]
# MAGIC 
# MAGIC def covariance(x, y):
# MAGIC     n = len(x)
# MAGIC     return dot(de_mean(x), de_mean(y)) / (n-1)
# MAGIC 
# MAGIC pageSpeeds = np.random.normal(3.0, 1.0, 1000)
# MAGIC purchaseAmount = np.random.normal(50.0, 10.0, 1000)
# MAGIC 
# MAGIC scatter(pageSpeeds, purchaseAmount)
# MAGIC 
# MAGIC covariance (pageSpeeds, purchaseAmount)

# COMMAND ----------

# MAGIC %md Now we'll make our fabricated purchase amounts an actual function of page speed, making a very real correlation. The negative value indicates an inverse relationship; pages that render in less time result in more money spent:

# COMMAND ----------

purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds

scatter(pageSpeeds, purchaseAmount)

covariance (pageSpeeds, purchaseAmount)

# COMMAND ----------

# MAGIC %md But, what does this value mean? Covariance is sensitive to the units used in the variables, which makes it difficult to interpret. Correlation normalizes everything by their standard deviations, giving you an easier to understand value that ranges from -1 (for a perfect inverse correlation) to 1 (for a perfect positive correlation):

# COMMAND ----------

def correlation(x, y):
    stddevx = x.std()
    stddevy = y.std()
    return covariance(x,y) / stddevx / stddevy  #In real life you'd check for divide by zero here

correlation(pageSpeeds, purchaseAmount)

# COMMAND ----------

# MAGIC %md numpy can do all this for you with numpy.corrcoef. It returns a matrix of the correlation coefficients between every combination of the arrays passed in:

# COMMAND ----------

np.corrcoef(pageSpeeds, purchaseAmount)

# COMMAND ----------

# MAGIC %md (It doesn't match exactly just due to the math precision available on a computer.)
# MAGIC 
# MAGIC We can force a perfect correlation by fabricating a totally linear relationship (again, it's not exactly -1 just due to precision errors, but it's close enough to tell us there's a really good correlation here):

# COMMAND ----------

purchaseAmount = 100 - pageSpeeds * 3

scatter(pageSpeeds, purchaseAmount)

correlation (pageSpeeds, purchaseAmount)

# COMMAND ----------

# MAGIC %md Remember, correlation does not imply causality!

# COMMAND ----------

# MAGIC %md ## Activity

# COMMAND ----------

# MAGIC %md numpy also has a numpy.cov function that can compute Covariance for you. Try using it for the pageSpeeds and purchaseAmounts data above. Interpret its results, and compare it to the results from our own covariance function above.

# COMMAND ----------

lets make a change