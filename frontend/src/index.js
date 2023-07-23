import React, { useEffect, useState } from "react";
import { render } from 'react-dom';

const UsersContext = React.createContext({
  users: [], fetchUsers: () => {}
})

export default function App() {
  const [users, setUsers] = useState([])
  const fetchUsers = async () => {
    const response = await fetch("http://localhost:8000/users")
    const users = await response.json()
    setUsers(users)
  }
  useEffect(() => {
    fetchUsers()
  }, [])
  
  return (
    <UsersContext.Provider value={{users, fetchUsers}}>
      <div>
      <pre>{JSON.stringify(users, null, 2)}</pre>
      </div>
      <div>
        <ul>
          {users.map((user) => (
            <li key={user.id}>
              {user.name},{user.email}
            </li>
          ))}
        </ul>
      </div>
    </UsersContext.Provider>
  )
}

const rootElement = document.getElementById("root")
render(<App />, rootElement)