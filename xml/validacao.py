#fazer pip install lxml
from lxml import etree

# indicar um documento XML
arquivo = "books.xml"

# definir um PARSER XML (Analisador)
parser = etree.XMLParser(dtd_validation=True)

try:
# executar a validacao
    tree = etree.parse(arquivo, parser)
    print("Documento XML Válido")

    titulos = tree.xpath(".//book[price<30]/title/text()")

    for titulo in titulos:
        print(titulo)
        sql = "insert into livros (titulo) values (\""+titulo+"\")"
        print(sql)

except Exception as error:
    print("Problema na validação ou leitura")
    print(error)