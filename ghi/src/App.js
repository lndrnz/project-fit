import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Homepage from './Homepage';
import Welcome from './Welcome'

function App() {
  return (
    <BrowserRouter>
        <div className="container">
          <Routes>
          <Route path="/" element={<Homepage />} />
          <Route path ="welcome" element={<Welcome />} />
          </Routes >
          </div>
    </BrowserRouter>
    
    
  );
}

export default App;
