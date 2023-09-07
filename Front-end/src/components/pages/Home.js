import React, { useEffect, useState, useRef } from 'react';
import { deleteMethod } from "../Django API/delete";
import axios from "axios";


export var i = [];


//Function to render the components 
const Home = () => {

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
  
  const formData = new FormData();
  formData.append('title', `${uniqueTitle}` );
  formData.append('description', `${i}`);
  
  try {
    const response = await fetch('http://localhost:8000/api/', {
      method: 'POST',
      body: formData
    })

    if (response.ok) {
      const data = await response.json();
      const xValue = data.x;
      console.log('Value of x:', xValue); 
      
    } else {
      console.log('Error:', response.statusText);
    }
  } catch (error) {
    console.log('Error:', error.message);
  }
}

async function fetchTodoList() {
  try {
    const response = await fetch('http://localhost:8000/api/back');
    const data = await response.json();
    console.log(data);
    setAnswer(data[0])
    if (data.length>0){
      let idToDelete = data[data.length - 1].id;
      // Send a DELETE request using axios
      axios.delete(`http://localhost:8000/api/back/delete/${idToDelete}/`)
      .then(response => {
        console.log('Delete successful:', response.data);
      })
      .catch(error => {
        console.error('Error:', error);
      });
      
    };

    return answer
  } catch (error) {
    console.log('Error:', error.message);
  }
}



//Post then let the values get treated and get the values back
async function postGet(){
  await postMethod()
  await fetchTodoList()
  
}

// Creates a dropdown menu so you can select which filter you want
function DropdownMenu({ inputId }) {
  const [selectedValue, setSelectedValue] = useState('Select an option');
  const inputValueRef = useRef('');

  if(selectedValue !=='Select an option' ){
    j.push(selectedValue)
    uniqueTitle = Array.from(new Set(j));
   
    
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

  const [filterCount, setFilterCount] = useState(0);
  const [todos, setTodos] = useState([]);
  const [answer, setAnswer] = useState(null);



  //Function to add filters menu 
  const handleAddFiltersClick = () => {
    setFilterCount((prevCount) => prevCount + 1);
    k=filterCount
    
  };

  //Function to get each value 
  const handleLogValues = () => {
    for (let index = 0; index < filterCount; index++) {
      const inputValue = document.getElementById(`myNumberInput-${index}`).value;
      i.push(inputValue)
      uniqueNb = Array.from(new Set(i));
    }
  };

 
  

  return (
    <div>
      <h1>Malkiel investment</h1>
      <h2>Filters:</h2>
      <button onClick={handleAddFiltersClick}>Add Filters</button>
      {Array.from({ length: filterCount }, (_, index) => (
        <DropdownMenu key={index} inputId={`myNumberInput-${index}`} />
      ))}
      
      <button onClick={()=>{handleLogValues();postGet()}}>Submit</button>
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
      {answer && (
        <div>
          <h1>ID: {answer.id}</h1>
          <p>Number: {answer.number}</p>
          <p>Description: {answer.description}</p>
        </div>
      )}
    </div>
  );
};

export default Home;


            