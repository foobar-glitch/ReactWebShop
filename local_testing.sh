mongosh mongodb://127.0.0.1 -u shopUser -p

use shop
db.products.find()
db.products.find().sort({ orderNumber: -1 })

db.products.find().sort({ numOrder: -1 }).limit(15)
#delete collection
db.products.deleteMany({})