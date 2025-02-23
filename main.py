from Functions.functions import *


def main():
    connection = Main("https://www.mercadolibre.com.co/ofertas#nav-header",".poly-component__title", ".andes-money-amount__fraction", 
                      "span.andes-money-amount.andes-money-amount--cents-superscript > span.andes-money-amount__fraction")
    connection.extract()

if __name__ == "__main__":
    main()
    
