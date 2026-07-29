"""
Calculate final price based on tax rate
"""

message = "Module imported"
print(message)

def main():
    print("Main function")

if __name__ == "__main__":
    main()

tax_rate = 0.1
def price_cal(price) :
    return price * (1 + tax_rate)