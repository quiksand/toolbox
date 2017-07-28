def ft_to_m(ft):
    m = 0.3048 * ft
    # print("{}m".format(m))
    return m

def ft_to_cm(ft):
    cm = 3.048 * ft
    # print("{}cm".format(cm))
    return cm

def m_to_ft(m):
    ft = m / 0.3048
    # print("{}'".format(ft))
    return ft

def m_to_in(m):
    inch = m / .0254
    # print("{}\"".format(inch))
    return inch

def cm_to_in(cm):
    inch = cm / 2.54
    # print("{}\"".format(inch))
    return inch

def mm_to_in(mm):
    inch = mm / 25.4
    # print("{}\"".format(inch))
    return inch

def m_to_ft_in(m):
    ft = m // 0.3048
    inch = (m % 0.3048) * 12
    # print("{}' {}\"".format(ft, inch))
    return ft, inch

def ft_in_to_m(ft, inch):
    ft += inch / 12
    m = 0.3048 * ft
    # print("{}m".format(m))
    return m

def ft_in_to_ft(ft, inch):
    ft += inch / 12
    # print("{}'".format(ft))
    return ft

def ft_in_to_in(ft, inch):
    inch += ft * 12
    # print("{}\"".format(inch))
    return inch

def in_to_m(inch):
    m = 0.3048 * inch / 12
    # print("{}m".format(m))
    return m

def in_to_mm(inch):
    mm = 304.8 * inch / 12
    # print("{}mm".format(mm))
    return mm

def in_to_cm(inch):
    cm = 30.48 * inch / 12
    # print("{}cm".format(cm))
    return cm

def in_to_ft(inch):
    ft = inch / 12
    # print("{}'".format(ft))
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
