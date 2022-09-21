from matplotlib import pyplot as plt

class Bond:

    def __init__(self):
        self.n = int(input("How many periods until maturity? (Enter -1 if unknown) "))
        self.ytm = float(input("What is the yield-to-maturity expressed as a percentage? (Enter -1 if unknown) "))
        self.pv = float(input("What is the present value of the bond? (Enter -1 if unknown) "))
        self.coupon = float(input("What is the payment per period? (Enter -1 if unknown) "))
        self.fv = float(input("What is the future value of the bond? (Enter -1 if unknown) "))

    def compute(self, value, n = None, ytm = None, pv = None, coupon = None, fv = None):
        value = value.upper()
        if n is None:
            n = self.n
        if ytm is None:
            ytm = self.ytm
        if pv is None:
            pv = self.pv
        if coupon is None:
            coupon = self.coupon
        if fv is None:
            fv = self.fv
        if value == "PV":
            pv = 0
            pv += (self.fv + self.coupon) / ((1 + self.ytm / 100) ** self.n)
            for i in range(1, self.n):
                pv += self.coupon / ((1 + self.ytm / 100) ** i)
            self.pv = pv
            print(f"The present value of a bond maturing in {self.n} periods with a periodic coupon rate of {self.coupon} priced to a yield of {self.ytm}% is {self.pv}")
        if value == "YTM":
            ytm = (self.coupon + ((self.fv - self.pv) / self.n)) / ((self.fv + self.pv) / 2)
            self.ytm = ytm
            print(f"The yield-to-maturity of a bond maturing in {self.n} periods with a periodic coupon rate of {self.coupon} and a present value of {self.pv} is {self.ytm:.6%}")
        if value == "COUPON":
            pass
        if value == "N":
            pass

    def constant_yield_price_trajectory(self): 
        ttm_price = {}
        for i in range(self.n, 0, -1):
            pv = (self.fv + self.coupon) / ((1 + self.ytm / 100) ** i)
            for j in range(1, i):
                pv += self.coupon / ((1 + self.ytm / 100) ** j) #add in smaller timesteps here somewhere
            ttm_price[i] = pv
        ttm_price[0] = self.fv
        fig, ax = plt.subplots()
        ax.plot(ttm_price.keys(), ttm_price.values(), marker = ".")
        ax.set_xlabel("Time to Maturity")
        ax.set_ylabel("Price per $100 of Par Value")
        ax.set_title("Constant-Yield Price Trajectory")
        fig.set_facecolor("lightsteelblue")
        plt.show()

    def approximate_convexity(self):
        pass
    def approximate_modified_duration(self):
        pass
    def approximate_macaulay_duration(self):
        pass


bond = Bond()
bond.compute("PV")
bond.constant_yield_price_trajectory()