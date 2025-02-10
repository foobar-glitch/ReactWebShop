import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

import './App.scss';
//import { Button, Alert, Breadcrumb, Card, Form, Container, Row, Col } from "react-bootstrap"
import "bootstrap/dist/css/bootstrap.min.css"
import Home from './components/Home';
import Header from './components/Header';

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        {/* This Header will appear on every route */}
        <Header />
        <div className="content">
          <Routes>
            <Route path="/" element={<Home />} />
          
          </Routes>
        </div>
      </div>
    </BrowserRouter>
  );

 /*
 
  return (
    <div className="App">
      <header className="App-header">
        <Container>
        <Form>
          <Row>
            <Col>
              <Form.Group controlId='formEmail'>
                <Form.Label>Email Address</Form.Label>
                <Form.Control type="email" placeholder='example@mail.com' />
                <Form.Text>
                  We'll never share youre email address, trust us!
                </Form.Text>
              </Form.Group>
            </Col>
            <Col>
              <Form.Group controlId='formPassword'>
                <Form.Label>Password</Form.Label>
                <Form.Control type="password" placeholder='password' />
              </Form.Group>
            </Col>
          </Row>
          <Button variant='secondary' type='submit'>Login</Button>
        </Form>
        <Card className='mb-5' style={{ color: 'green'}}>
          <Card.Img src="https://picsum.photos/300/100"/>
          <Card.Body />
          <Card.Title style={{ color: 'blue'}}>
            Card Example
          </Card.Title>
          <Card.Text>
            This is an eample of react bootstrap cards
          </Card.Text>
          <Button variant='primvary'>Read More</Button>

        </Card>
        <Breadcrumb>
          <Breadcrumb.Item>Test</Breadcrumb.Item>
          <Breadcrumb.Item> Test 2</Breadcrumb.Item>
          <Breadcrumb.Item active> Test 3</Breadcrumb.Item>
        </Breadcrumb>
        <Alert variant='success'> This is a button</Alert>
        <Button> Test Button</Button>
        </Container>
      </header>
    </div>
  );
 */
}

export default App;
