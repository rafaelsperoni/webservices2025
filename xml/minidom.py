from xml.dom import minidom

doc = minidom.parse("books.xml")

# doc.getElementsByTagName returns the NodeList
descricao = doc.getElementsByTagName("description")[0]
print(descricao.firstChild.data)

books = doc.getElementsByTagName("book")
for book in books:
    title = book.getElementsByTagName("title")[0]
    language = title.getAttribute("lang")
    price = book.getElementsByTagName("price")[0]
    print("Título:% s, idioma:% s, preço:% s" %
              (title.firstChild.data, language, price.firstChild.data))