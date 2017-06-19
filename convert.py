
def ft_to_m(ft):
    m = 0.3048 * ft
    # print("{}m".format(m))
    return m

def m_to_ft(m):
    ft = m / 0.3048
    # print("{}'".format(ft))
    return ft

def m_to_ft_in(m):
    ft = m // 0.3048
    inch = (m % 0.3048) * 12
    # print("{}' {}\"".format(ft, inch))
    return ft, inch

def ft_in_to_m(ft, inch):
    ft += inch / 12
    m = 0.3048 * ft
    # print("{}m.format(m))
    return m

def in_to_m(inch):
    m = 0.3048 * inch / 12
    # print("{}m.format(m))
    return m

def in_to_ft(inch):
    ft = inch / 12
    # print("{}'.format(ft))
    return ft

def in_to_ft_in(inch):
    ft = inch // 12
    inch = inch % 12
    # print("{}' {}\"".format(ft, inch))
    return ft, inch

def main():
    print()

if __name__ == '__main__':
    main()