import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Homepage from './Homepage';

function App() {
  return (
    <BrowserRouter>
        <div className="container">
          <Routes>
          <Route path="/" element={<Homepage />} />
          </Routes >
          </div>
    </BrowserRouter>
    
    
  );
}

export default App;
