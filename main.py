def aznum(num):
    az = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s = 1
    m_list = []
    while s != 0:
        r = num // 26
        c = num - r * 26
        if c == 0:
            c = 26
            r = r - 1
        num = r
        if c != 0:
            m_list.append(c)
        if num <= 25:
            m_list.append(r)
            s = 0
    if 0 in m_list:
        m_list.remove(0)
    m_list = reversed(m_list)
    ret = ''
    for i in m_list:
        ret += az[i - 1]
    return ret


x = 17577
print(x, aznum(x))
