import React, { useState } from "react";
import { Container, Row, Col, Button } from "react-bootstrap";
import { useNavigate } from "react-router-dom";
import Rating from '@mui/material/Rating';
import useFetchGET from "./useFetchGET";
import { product_overview } from "./Universals";


const ArticleShowCase = (articles, OpenProduct) => {
    return(<>
        {articles.map((art) => (
        <Col  xs={2} md={2} lg={2} className="article-column" onClick={() => OpenProduct(art["productId"])}>
            <Row className="preview-picture">
                <img src={`${product_overview}/${art["productId"]}`} alt="notfound.png" />
            </Row>
            <Row className="product">
                {art["product"]}
            </Row>
            <Row className="rating">
                <Rating className="rating-stars" name="read-only" precision={0.1} value={Number(art["rating"])} readOnly />
                <div className="rating-value">{art["rating"]}/5 ({art["numRatings"]})</div>
            </Row>
            <Row className="price">
                {art["price"]}
            </Row>
        </Col>
        ))}
    </>)
}

function getSubarray(array, start, length){
    if(start+length>= array.length){
        return array.slice(start, array.length - 1)
    }
    return array.slice(start, start+length)
}


const ArticleContainer = (article_endpoint, category)  => {
    const [startSlide, setStartSlide] = useState(0);

    // length how many articles shown
    const length = 4;
    const { data, isPending, error }= useFetchGET(article_endpoint)
    

    const navigate = useNavigate();

    const moveRight = (maxLength) => {
        if(startSlide+length < maxLength){
            setStartSlide(startSlide+length)
        }
        console.log(startSlide)
    }

    const moveLeft = () => {
        if(startSlide-length<=0){
            setStartSlide(0)
        }else{
            setStartSlide(startSlide-length)
        }
        console.log(startSlide)
    }

    const OpenProduct = (product_id) => {
        console.log(product_id)
        navigate(`/product/${product_id}`);
    }
    return (data && !isPending && !error && data.status == 200 && <>
     <Container className="article-container">
        <Row className="article-header">
            <Col className="category">
                <h3><b>{category}</b></h3>
            </Col>
            <Col className="slide">
                <Button style={{marginRight: "5px"}} onClick={moveLeft}>
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-left-square" viewBox="0 0 16 16">
                        <path fill-rule="evenodd" d="M15 2a1 1 0 0 0-1-1H2a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1zM0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2zm11.5 5.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5z"/>
                    </svg>
                </Button>
                <Button onClick={() => moveRight(data.message.length)}>
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right-square" viewBox="0 0 16 16">
                        <path fill-rule="evenodd" d="M15 2a1 1 0 0 0-1-1H2a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1zM0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2zm4.5 5.5a.5.5 0 0 0 0 1h5.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3a.5.5 0 0 0 0-.708l-3-3a.5.5 0 1 0-.708.708L10.293 7.5z"/>
                    </svg>
                </Button>
            </Col>
        </Row>
        <Row className="articles">
            {ArticleShowCase(getSubarray(data.message, startSlide, length), OpenProduct)}
        </Row>
    </Container>
    </>
    );
}
export default ArticleContainer;