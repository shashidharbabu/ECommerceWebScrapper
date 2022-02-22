from requests_html import HTMLSession
s= HTMLSession()


#Defining a function to give product as input

#URL= https://themes.woocommerce.com/storefront/?s={product}&post_type=product

def get_product_links(product):
    url=f'https://themes.woocommerce.com/storefront/?s={product}&post_type=product'

#Creating lists for links and model names and creating dictionary for zipping both model and url together

    links=[]
    models=[]
    dic={}

#Requesting URL and selecting the product element by it's attributes

    r=s.get(url)
    products= r.html.find('ul.products li')

#for loop to append each link into 'links' list and model name into 'models' list
    for item in products:
        links.append(item.find('a', first= True).attrs['href'])
        models.append(item.find('h2.woocommerce-loop-product__title', first= True).text)

        #for loop to zip both lists together into a dictionary

        for i in range(0,len(models)):
            dic[models[i]] = links[i]
        dic=dict(zip(models,links))

    return dic

#Giving input product name

product1= get_product_links('shirt')
print(product1)