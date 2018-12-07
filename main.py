import enum
print('\t\t\t   Powered by RetailCook\n\t\t\thttps://vk.com/retail_plus')


def main():
    fullname = str(input('\n\nPlease Enter Full Name: '))
    email = str(input('Please Enter Email: '))
    tel = str(input('Please Enter Telephone Number: '))
    address = str(input('Please Enter Address: '))
    address2 = str(input('Please Enter Address2: '))
    address3 = str(input('Please Enter Address3: '))
    city = str(input('Please Enter City: '))
    postcode = str(input('Please Enter Postcode: '))
    cardtype = str(input('Please Enter Cardtype (visa, mastercard, american express, solo): '))
    cardnumber = str(input('Please Enter Cardnumber: '))
    expirydate = str(input('Please Enter card date (12/2018): '))
    cvv = str(input('Please Enter CVV: '))
    token = str(input('Please Enter Your Token: '))
    checkoutlink = 'https://www.supremenewyork.com/checkout?utf8=?&authenticity_token={0}&order[billing_name]={1}&order[email]={2}&order[tel]={3}&order[billing_address]={4}&order[billing_address_2]={5}&order[billing_address_3]={6}&order[billing_city]={7}&order[billing_zip]={8}&order[billing_country]=RU&same_as_billing_address=1&store_credit_id=&credit_card[type]={9}&credit_card[cnb]={10}&credit_card[month]={11}&credit_card[year]=2018&credit_card[vval]={12}&order[terms]=0&hpcvv=&cnt=1'.format(token, fullname, email, tel, address, address2, address3, city, postcode, cardtype, cardnumber, expirydate.split('/'[0]), cvv)
    save = str(input('Save url in text file .txt? (y/n)'))
    if save.strip().startswith('y'):
        open('CheckoutLink', 'w', encoding='utf-8').write(checkoutlink)
    else:
        print('\n{0}'.format(checkoutlink))


if __name__ == '__main__':
    main()
