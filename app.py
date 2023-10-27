from flask import Flask , jsonify ,request
#class Flask

#Create a instance of class Flask
app = Flask(__name__)
# print(__name__)

books = [
    {"id":1,'title':'Book 1','author':'Author 1'},
    {"id":2,'title':'Book 2','author':'Author 2'},
    {"id":3,'title':'Book 3','author':'Author 3'},
    {"id":4,'title':'Book 4','author':'Author 4'},
    
]

@app.route('/',methods=['GET'])
def homepage():
    return 'Home page'

#route to get all books
# jsonify is a function that converts the Python dictionary into a JSON response.
#  This is necessary because HTTP is a text protocol. Therefore, when you send data over HTTP, it needs to be a string.
@app.route('/books',methods=['GET'])
def get_books():
    return jsonify(books)

#route to get a specific book by ID
@app.route('/books/<int:book_id>',methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify(book)
        
    return jsonify({'error':'Book not found'})

#route to add a new book
@app.route('/books',methods=['POST'])
def add_book():
    print(request.json["id"])
    new_book = {
        "id":request.json["id"],
        "title":request.json['title'],
        "author":request.json['Author']

    }
    books.append(new_book)
    return jsonify({'message':'Book added sucessfully'})

#ROUTE TO UPDATE THE EXISTING BOOK
@app.route('/books/<int:book_id>',methods=['PUT'])
def update_book(book_id):
    for book in books:
        if book['id'] == book_id:
            book['title'] = request.json['title']
            book['Author'] = request.json['Author']
            return jsonify({'message':'Book added sucessfully'})
    return jsonify({'message':'Book Not Found'})


#route to delete a book
@app.route('/books/<int:book_id>',methods=['DELETE'])
def delete_book(book_id):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return jsonify({'message':'Book Removed Sucessfully'})
    return jsonify({'message':'Book Not Found'})




if __name__=='__main__':
    app.run(debug=True)