import React from 'react';
import { Container, Button } from 'react-bootstrap';

const SimplePage: React.FC = () => {
    return (
        <Container>
            <h1>Simple Page</h1>
            <p>This is a simple page using React, TypeScript, and React Bootstrap.</p>
            <Button variant="primary">Click Me</Button>
        </Container>
    );
};

export default SimplePage;