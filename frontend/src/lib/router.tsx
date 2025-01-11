import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import SimplePage from '../shared_components/pages/simple';
import SimpleLayout from '../layouts/simple';
// import FilesManagementPage from '../features/file_managements/pages/FilesMangementPage';

const AppRouter: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path='' element={<SimpleLayout />}>
            <Route path='' element={<SimplePage />} />
            {/* <Route path='files' element={<FilesManagementPage />} /> */}
        </Route>

        <Route path='*' element={<SimpleLayout />}>
        </Route>
      </Routes>
    </Router>
  );
};

export default AppRouter;
