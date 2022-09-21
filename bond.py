from matplotlib import pyplot as plt

class Bond:

    def __init__(self):
        self.n = int(input("How many periods until maturity? (Enter -1 if unknown) "))
        self.ytm = float(input("What is the yield-to-maturity expressed as a percentage? (Enter -1 if unknown) "))
        self.pv = float(input("What is the present value of the bond? (Enter -1 if unknown) "))
        self.coupon = float(input("What is the payment per period? (Enter -1 if unknown) "))
        self.fv = float(input("What is the future value of the bond? (Enter -1 if unknown) "))

    def compute(self, value):
        value = value.upper()
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
    def approximate_modified_duration(self, dyield = 0.0001):
        pv0 = self.pv
        ytmdown = (1 + (self.ytm / 100) - dyield)
        ytmup = (1 + (self.ytm / 100) + dyield)
        pvdown = (self.fv + self.coupon) / (ytmdown ** self.n)
        pvup = (self.fv + self.coupon) / (ytmup ** self.n)
        for i in range(1, self.n):
            pvdown += self.coupon / (ytmdown ** i)
            pvup += self.coupon / (ytmup ** i)
        approx_mod_dur = (pvdown - pvup) / (2 * pv0 * dyield)
        self.approx_mod_dur = approx_mod_dur
        return approx_mod_dur
    def approximate_macaulay_duration(self):
        approx_mod_dur = self.approximate_modified_duration()
        approx_mac_dur = (1 + self.ytm / 100) * approx_mod_dur
        self.approx_mac_dur = approx_mac_dur
        return approx_mac_dur


if __name__ == "__main__":
    bond = Bond()
    bond.compute("PV")
    # bond.constant_yield_price_trajectory()
    print(f"The approx mod dur is: {bond.approximate_modified_duration()}, approx mac dur: {bond.approximate_macaulay_duration()}")