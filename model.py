class LinearRegression:
    def __init__(self):
        self.coef_ = []
        self.intercept = 0.0
        self.history = []
        self.lr=None

    def predic(self,x):
        y_hat= self.coef_ * x + self.intercept

    def cost(self,x,y):
        y_hat = self.predic(x)
        error= y-y_hat
        error2= error**2
        return np.mean(error2
                       )