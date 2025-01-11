import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import SimplePage from '../pages/simple';
import SimpleLayout from '../layouts/simple';

const AppRouter: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path='simple' element={<SimpleLayout />}>
            <Route path='' element={<SimplePage />} />
        </Route>
      </Routes>
    </Router>
  );
};

export default AppRouter;
