require('dotenv').config(".env");

const MongoSecrets = {
    HOST: process.env.MONGO_HOST,
    PORT: process.env.MONGO_PORT,
    USER: process.env.MONGO_USER,
    USER_PASSWORD: process.env.MONGO_USER_PASSWORD,
    DB_NAME: process.env.MONGO_DB_NAME,
};

const MongoCollections = {
    SHOP_ENTRIES: process.env.MONGO_COLLECTION_NAME
}

module.exports = {
    MongoSecrets,
    MongoCollections
}



