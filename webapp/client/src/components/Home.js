import React from "react";
import { Container} from "react-bootstrap";
import ArticleContainer from "./ArticleContainer";
import { popular_subcategories } from "./Universals";

const Home = () => {
    return (
        <Container className="home" >
           {ArticleContainer(`${popular_subcategories}/washingmachine`, "WASHING MACHINES")}
        </Container>
    )

}

export default Home;