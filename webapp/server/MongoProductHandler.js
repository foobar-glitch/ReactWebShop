const { MongoClient, ObjectId } = require('mongodb');
const { MongoSecrets, MongoCollections } = require('./DBConfigs');
const uri = `mongodb://${MongoSecrets.USER}:${MongoSecrets.USER_PASSWORD}@${MongoSecrets.HOST}:${MongoSecrets.PORT}`;
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });


async function getPopularSubCategory(sub_cat) {
    try {
        await client.connect();
        const database = client.db(MongoSecrets.DB_NAME);
        const collection = database.collection(MongoCollections.SHOP_ENTRIES);
    
        // Retrieve all documents from the collection
        let collection_entries;
        if(sub_cat){
            collection_entries = await collection.find({subcategory: sub_cat}).sort({ numOrder: -1 }).limit(15).toArray();
            return collection_entries
        }else{
            console.log(`Subcategory '${sub_cat}'`)
            return;
        }

        // Display the retrieved documents
        } finally {
            await client.close();
        }
}


module.exports = {
    getPopularSubCategory,
}