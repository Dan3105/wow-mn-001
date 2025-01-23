import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import SimplePage from '../shared_components/pages/simple';
import MainPage from '@/pages/main/main_page';
import FilesManagementPage from '@/pages/files_management/files_management_page';

const AppRouter: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path='' element={<MainPage />}>
            <Route path='my-docs' element={<FilesManagementPage />} />
            <Route path='*' element={<SimplePage />} />
        </Route>
      </Routes>
    </Router>
  );
};

export default AppRouter;
