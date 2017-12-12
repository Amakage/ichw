def answer(s):
    """get string from the web"""
    from urllib.request import urlopen
    doc = urlopen(s)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return jstr

def get_amount(s):
    """get the amount of money from the string"""
    s=s.split('"')
    at_list=s[7]
    at_str=at_list.split()
    at=float(at_str[0])
    return at

def exchange(cf, ct, amount):
    """input Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    input Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    input Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float

    The value returned has type float."""

    a=str(amount)
    web=('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+cf+'&to='+ct+'&amt='+a)
    s=answer(web)
    at=get_amount(s)
    return at


def test_answer():
    """test whether answer works"""
    assert(answer('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=EUR&amt=2.5')=='{ "from" : "2.5 United States Dollars", "to" : "2.0952375 Euros", "success" : true, "error" : "" }')
    assert(answer('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=EUR&amt=2.1')=='{ "from" : "2.1 United States Dollars", "to" : "1.7599995 Euros", "success" : true, "error" : "" }')
    assert(answer('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=CNY&to=EUR&amt=8.8')=='{ "from" : "8.8 Chinese Yuan", "to" : "1.1301051921884 Euros", "success" : true, "error" : "" }')

def test_get_amount():
    """test whether amount works"""
    assert(get_amount('{ "from" : "2.5 United States Dollars", "to" : "2.0952375 Euros", "success" : true, "error" : "" }')== 2.0952375)
    assert(get_amount('{ "from" : "2.1 United States Dollars", "to" : "1.7599995 Euros", "success" : true, "error" : "" }')== 1.7599995)
    assert(get_amount('{ "from" : "8.8 Chinese Yuan", "to" : "1.1301051921884 Euros", "success" : true, "error" : "" }')== 1.1301051921884)

def test_exchange():
    """test whether exchange works"""
    assert(exchange('USD','EUR',2.5)== 2.0952375)
    assert(exchange('USD','EUR',2.1)== 1.7599995)
    assert(exchange('CNY','EUR',8.8)== 1.1301051921884)

def testALL():
    """test all cases"""
    test_answer()
    test_get_amount()
    test_exchange()
    print("All tests passed")

testALL()
