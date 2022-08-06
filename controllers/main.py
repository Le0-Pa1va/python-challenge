import bs4


# Read html
e_commerce_html = open('pages/content.html', 'r')

# Parse html
soup = bs4.BeautifulSoup(e_commerce_html.read(), 'html.parser')


def get_product_name(href):
    """Returns the product's name

    Args:
        href (str): Product's url.

    Returns:
        String: Product's name
    """

    product_data = soup.find('a', {'href': href}, 'img')
    return product_data.img['alt']


def get_product_price(a):
    """Get the product's price

    Args:
        a (bs4.element.Tag): The whole tag <a> of the product

    Returns:
        Float: Product's price
    """

    # Getting the int part of the price
    price_whole = (a.find('span', {'class': 'a-price-whole'}).text).replace('.', '')

    #Getting the cents part of the price
    price_fraction = a.find('span', {'class': 'a-price-fraction'}).text

    # Putting the above parts together and converting to float
    total_price = float(price_whole.replace(',', '') + '.' + price_fraction)

    return total_price


def get_best_selling_products(product_id):
    """Returns if the product is a best-seller

    Args:
        product_id (string): Product's id

    Returns:
        Bool: Returns True if it's a best-seller else returns False.
    """

    # Looking for the span with the id equals to the product's id concatenated with the string '-best-seller'
    product_data = (soup.find('span', {'id': f'{product_id}-best-seller'}))
    if not product_data:
        return False
    else:
        return True


def get_product_rating(href):
    """Returns the product rating

    Args:
        href (string): Product's url

    Returns:
        Float: Rating value.
    """

    product_data = soup.find_all('div', {'class': 'a-row a-size-small'})
    for item in product_data:
        if item.find_all('a', {'href': href+'#customerReviews'}):
            return float(item.text.split()[0].replace(',', '.'))


def build_product_dict(name, price, best_seller, product_rating):
    """Build the product dict that will be added to the product list

    Args:
        name (string): Product's name
        price (float): Product's price
        best_seller (bool): Variable that tells if the product is a best-seller
        product_rating (float): Product's rating

    Returns:
        Dict: Dict with all products attributes.
    """

    product_dict = {
        'name': name,
        'price': price,
        'best_seller': best_seller,
        'product_rating': product_rating,
    }

    return product_dict


def list_products(**kwargs):
    """Returns a list of products given the arguments

    Args:
        best_seller (bool, optional): Get only the best-selling products if it's true. Defaults to False.
        rating (float, optional): Get only the products with a rating higher than the given value. Defaults to None.
        name (string, optional): List only the information of a single product, given its name. Defaults to None.

    Returns:
        [List]: List of products based on the given args.
    """

    # Getting the tag <a> that we can get some useful information.
    products_data = soup.find_all('a', {'class': 'a-size-base a-link-normal a-text-normal'}, href=True)

    product_list = []
    for a in products_data:
        product_href = a['href']
        product_id = product_href.split('/')[3]

        # Getting the product attributes
        product_name = get_product_name(product_href)
        total_price = get_product_price(a)
        best_seller_product = get_best_selling_products(product_id)
        product_rating = get_product_rating(product_href)

        # Checking if we have to filter the  best-selling products
        if kwargs.get('best_seller') == 'true':
            if best_seller_product == True:

                # Getting the best-selling products
                product_dict = build_product_dict(product_name, total_price, best_seller_product, product_rating)
            else:
                continue

        # Checking if we have to filter the products by the rating
        if kwargs.get('rating'):
            if product_rating > float(kwargs.get('rating')):

                # Getting the products with the rating higher than the given one
                product_dict = build_product_dict(product_name, total_price, best_seller_product, product_rating)
            else:
                continue

        # Checking if we have the product by its name
        if kwargs.get('name'):
            if product_name == kwargs.get('name'):

                # Getting only the product with the given name
                product_dict = build_product_dict(product_name, total_price, best_seller_product, product_rating)
            else:
                continue

        else:
            # Getting all products if there is no filter
            product_dict = build_product_dict(product_name, total_price, best_seller_product, product_rating)

        # Adding the products to the list
        product_list.append(product_dict)

    # This should return the list of products
    return product_list
