import React from 'react';
import { Outlet } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';

const SimpleLayout: React.FC = () => {
    return (
        <div className="vh-100 vw-100 d-flex flex-column">
            {/* <Navbar bg="dark" variant="dark">
                <Nav>
                    <Nav.Link as={Link} to="/chat">Chat</Nav.Link>
                    <Nav.Link as={Link} to="/files">Files Management</Nav.Link>
                </Nav>
            </Navbar> */}
            <div className="flex-grow-1">
                <Outlet />
            </div>
        </div>
    );
};

export default SimpleLayout;
