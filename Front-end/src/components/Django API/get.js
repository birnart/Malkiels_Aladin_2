
export async function fetchTodoList() {
    try {
      const response = await fetch('http://localhost:8000/api/');
      const data = await response.json();
      console.log(data);
      return data;
    } catch (error) {
      console.log('Error:', error.message);
    }
  }