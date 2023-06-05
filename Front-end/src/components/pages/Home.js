import React, { useEffect, useState, useRef } from 'react';
//import { postMethod } from "../Django API/post";
import { fetchTodoList } from "../Django API/get";
import { deleteMethod } from "../Django API/delete";


export var i = [];
var j = []
var k;
var uniqueTitle = []
var uniqueNb = []

// Gives all the filters possible
var options = [
  { value: 'CAPM', label: 'CAPM' },
  { value: 'Beta', label: 'Beta' },
  { value: 'Volatility', label: 'Volatility' }
];

// Function to post the filters and the value to the API 
async function postMethod() {
  console.log(i);
  const formData = new FormData();
  formData.append('title', `${uniqueTitle}` );
  formData.append('description', `${i}`);
  
  try {
    const response = await fetch('http://localhost:8000/api/', {
      method: 'POST',
      body: formData
    });

    if (response.ok) {
      const data = await response.json();
      console.log(data.id);
    } else {
      console.log('Error:', response.statusText);
    }
  } catch (error) {
    console.log('Error:', error.message);
  }
}

// Creates a dropdown menu so you can select which filter you want
function DropdownMenu({ inputId }) {
  const [selectedValue, setSelectedValue] = useState('Select an option');
  const inputValueRef = useRef('');

  if(selectedValue !=='Select an option' ){
    j.push(selectedValue)
    uniqueTitle = Array.from(new Set(j));
    console.log(uniqueTitle);
    
  }
  
  // Deletes the filter option when selected
  options = options.filter(option => option.value !== selectedValue);
  
  return (
    <div>
      <select
        value={selectedValue}
        onChange={(e) => setSelectedValue(e.target.value)}
      >
        <option>{selectedValue}</option>
        {options.map((option) => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>
      <input
        type="number"
        id={inputId}
        min="0"
        max="100"
        step="1"
        ref={inputValueRef}
      />
    </div>
  );
}

//Function to render the components 
const Home = () => {

  const [filterCount, setFilterCount] = useState(0);
  const [todos, setTodos] = useState([]);

  const handleReload = () => {
    window.location.reload();
  };

  //Function to add filters menu 
  const handleAddFiltersClick = () => {
    setFilterCount((prevCount) => prevCount + 1);
    k=filterCount
    console.log(k);
  };

  //Function to get each value 
  const handleLogValues = () => {
    for (let index = 0; index < filterCount; index++) {
      const inputValue = document.getElementById(`myNumberInput-${index}`).value;
      console.log(`Input ${index + 1} value:`, inputValue);
      i.push(inputValue)
      uniqueNb = Array.from(new Set(i));
      console.log(uniqueNb);
      console.log(i);
    
      
    }
  };

 
  //Used to update the new input and put it on the website. Not useful because it wont be displayed
  useEffect(() => {
    async function fetchTodos() {
      try {
        const res = await fetch('http://127.0.0.1:8000/api/');
        const todosData = await res.json();
        setTodos(todosData);
      } catch (error) {
        console.log(error);
      }
    }

    fetchTodos();
  }, []);

  return (
    <div>
      <h1>Malkiel investment</h1>
      <h2>Filters:</h2>
      <button onClick={handleAddFiltersClick}>Add Filters</button>
      {Array.from({ length: filterCount }, (_, index) => (
        <DropdownMenu key={index} inputId={`myNumberInput-${index}`} />
      ))}
      
      <button onClick={()=>{handleLogValues();postMethod();handleReload()}}>Submit</button>
        <button onClick={fetchTodoList}>List</button>
        <textarea id='delete' ></textarea>
          <button onClick={deleteMethod}>Delete</button>
          <div>
          {todos.map((item) => (
          <div key={item.id}>
            <h1>{item.title}</h1>
            <span>{item.description}</span>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Home;


            