'''

from sklearn.feature_selection import SelectKBest, f_classif
selector = SelectKBest(score_func=f_classif, k=2)
X_new = selector.fit_transform(X, y)


from sklearn.feature_selection import SelectPercentile, f_classif
selector = SelectPercentile(score_func=f_classif, percentile=10)
X_new = selector.fit_transform(X, y)
'''