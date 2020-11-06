# -*- coding: utf-8 -*-


class Model(object):
    """Main model class

    <INSERT HERE THE DESCRIPTION OF HOW TO LOAD A TRAINED MODEL>
    """
 
    def __init__(self, **kwargs):
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.model = object(
                        n_estimators=self.n_trees,
                        max_depth=self.max_depth,
                        )

    def fit(self, X, y):
        self.model.fit(X, y)
        return self

    def predict_proba(self, X):
        return self.model.predict_proba(X)

    def predict(self, X):
        """Predictions method

        Parameters
        ----------
        <DESCRIBE HERE YOUR INPUT DATA AND EXAMPLES>

        Returns
        ----------
        <DESCRIBE HERE YOUR OUTPUT DATA AND EXAMPLES>
        """
        return self.model.predict(X)
