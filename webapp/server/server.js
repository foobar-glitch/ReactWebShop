var session = require('express-session')
const express = require('express');
const cors = require('cors');
const crypto = require('crypto');
const { COOKIE_EXPIRAION_TIME_MS } = require('./server_constants');
const { getPopularSubCategory } = require('./MongoProductHandler');
const path = require('path');

const local_domain = "http://localhost:3000"
//const remote_domain = "http://[2a02:908:e845:3560::8070]:80"
const server_domain = local_domain

function generateRandomString(length) {
    return crypto.randomBytes(length).toString('hex').slice(0, length);
}


const app = express();
app.set('trust proxy', 1)

const crypto_secret = generateRandomString(32)

console.log(crypto_secret)

app.use(session({
	secret: crypto_secret,
	resave: true,
	saveUninitialized: true,
    cookie: { maxAge: COOKIE_EXPIRAION_TIME_MS, sameSite: 'Strict', secure: false }
}));

app.use(cors({
    origin: server_domain,
    credentials: true
}));

app.get('/popular/:subcategory', async (req, res) => {
    const subcategory = req.params.subcategory;
    const popular_sub_cat = await getPopularSubCategory(subcategory);
    overview_message = popular_sub_cat.map(({ _id, numOrder, features, description, ...rest }) => rest);
    return res.json({
        status: 200,
        message: overview_message
    })
})

app.get('/file/product/overview/:id', async (req, res) => {
    const fileId = req.params.id;
    const filePath = path.join(__dirname, 'images', 'products', 'productId', fileId, '1.png');
    
    res.sendFile(filePath, err => {
        if (err) {
          res.json({
            status: 404,
            message: "File not found"
          })
        }
    });
})

app.listen(8080, () => {
    console.log(`Server is running on port 8080.`);
});
