import React, { Component } from "react"
import Button from 'react-bootstrap/Button';


class HomePage extends Component {
    render() {
      const myStyle={
        backgroundImage: 
  "url('https://wallpaperaccess.com/full/3702281.jpg')",
        marginTop:'-70px',
        fontSize:'50px',
        backgroundPosition: 'center',
        backgroundSize: 'cover',
        backgroundRepeat: 'no-repeat',
        width: '100vw',
        height: '100vh'
    };
    return (
  
      <div style={myStyle}>
      <div className="row"> 
        <h1 className="text-center" style={{color: 'white', textAlign: 'center'}}>Tren</h1>
        <div className="col-lg-6 mx-auto">
          <p className="lead fw-bold" style={{color: 'white', fontWeight: "bold", textAlign: 'center'}}>
            The beginning of your journey to Ascend.
          </p>
  <button className="text-center"  style={{ backgroundColor: "lightgrey", color: "black", padding: "15px 32px", marginInline: "auto", display: "flex", fontSize: "30px", fontWeight: "bold", borderRadius: "12px" }}>Start here..</button>
        </div>
      </div>
      </div>
    );
  }
  }
  export default HomePage;