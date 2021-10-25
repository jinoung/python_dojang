files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', 'table.xslx', 'spec.docx']
print(list(filter(lambda x: x.find('.jpg') != -1 or x.find('.png') != -1, files)))
