import React from 'react';
import { Outlet, Link } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Navbar, Nav } from 'react-bootstrap';

const SimpleLayout: React.FC = () => {
    return (
        <div className="vh-100 vw-100 d-flex flex-column">
            <Navbar bg="dark" variant="dark">
                <Nav>
                    {/* <Nav.Link as={Link} to="/simple">Home</Nav.Link> */}
                    {/* <Nav.Link as={Link} to="/features">Features</Nav.Link> */}
                    {/* <Nav.Link as={Link} to="/pricing">Pricing</Nav.Link> */}
                </Nav>
            </Navbar>
            <div className="flex-grow-1">
                <Outlet />
            </div>
        </div>
    );
};

export default SimpleLayout;
