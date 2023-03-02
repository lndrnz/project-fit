import React, { useState } from "react"



const products = [
  { title: 'Cabbage', isFruit: false, id: 1 },
  { title: 'Garlic', isFruit: false, id: 2 },
  { title: 'Apple', isFruit: true, id: 3 },
];

const listItems = products.map((product) =>
<li key={product.id}
        style=
        {{
        color: product.isFruit ? 'blue':'red',
        fontSize: '80px'}}>
  {product.title}</li>)



function HomePage(props) {
    const [isHungry, setHungry] = useState(true)
    return (
      
      <>
      <header style={{color: 'purple', fontSize: '80px', textAlign: 'center'}}>Cookbook</header>
      <ul style = {{ fontSize: '80px'}}>Are you hungry for this?{listItems}</ul>
      <button onClick={() => {setHungry(false)}} disabled={!isHungry} style={{color: isHungry === true ? 'red': 'green'}}>
        {isHungry ? "I am hungry" : "I am not hungry"} 
      </button>


      </>

      

    );
  }
  export default HomePage;