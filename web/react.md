REACT
===============================================================================

[TOC]

-------------------------------------------------------------------------------
# How To

## Building a react autocomplete component

**Reference:**
https://blog.bitsrc.io/building-a-react-autocomplete-component-from-scratch-3f4d5618aa14?utm_medium=email&utm_source=topic+optin&utm_campaign=awareness&utm_content=20190306+web+nl&mkt_tok=eyJpIjoiTjJRd01tUTFObVkzWmpSaCIsInQiOiJyY25hUTFcL2VDNndHQXpXSWJ0QW54ZHpGSkhMQzhYXC9XQk5Fbkl6ekdwNGl2M1JYOTNxbUQrRVY4Y0xGSmZsXC9sb1owV2tkS1VjdU5LeDljdFhpZ1Y1Ym9pUTRzUzFYa0h1K1ZCV0k0Y1pXR0t1Y2hqaHhTaG8yamhrSmdcL0RTXC9kIn0%3D


## Introducing Hooks

https://reactjs.org/docs/hooks-intro.html


## How to Get Started With React Hooks: Controlled Forms

**Sample:**
```
import React, { useState } from "react";
import "./styles.css";
function Form() {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
return (
    <form>
      <input
        value={firstName}
        onChange={e => setFirstName(e.target.value)}
        placeholder="First name"
        type="text"
        name="firstName"
        required
      />
      <input
        value={lastName}
        onChange={e => setLastName(e.target.value)}
        placeholder="Last name"
        type="text"
        name="lastName"
        required
      />
      <input
        value={email}
        onChange={e => setEmail(e.target.value)}
        placeholder="Email address"
        type="email"
        name="email"
        required
      />
      <input
        value={password}
        onChange={e => setPassword(e.target.value)}
        placeholder="Password"
        type="password"
        name="password"
        required
      />
<button type="submit">Submit</button>
    </form>
  );
}
export default Form;
```

While that part of the code looks strange at first, it is simple to understand. 
- We are no longer declaring a single object called state that holds our component’s state. 
- Instead, we are now splitting up state into multiple declarations.

Say we wanted to declare a state variable called firstName the familiar extends React.Component way, we’d usually do it in the constructor and then access it by writing this.state.firstName.
- But with useState, we initialize two variables called firstName and setFirstName. We then set their values to whatever useState() returns.
- Why do we have to declare setFirstName too though?
- Well, since this is a functional component, we don’t have setState to help us modify the value of the state variable. What we do have is setFirstName whose sole purpose is to update firstName every time we call it.

So when you see:
```
const [firstName, setFirstName] = useState("")
```

- We’re basically declaring a state variable and a function to allow us to modify the state variable later. 
- The empty string in the useState call is the initial value of firstName and can be set to any required value. 
- Note that you can name the setFirstName function whatever you want. It is a convention, however, to append ‘set’ before the name of the state variable we’re modifying.

We now know how to create a state variable in a functional component and how to update it. Let’s continue by explaining the rest of the code.
- In our first input tag, we set it’s value to the state variable we declared at the top of our component. As for the onChange handler, we set it to an arrow function that calls the function which updates our state variable for us.
- Where we had a method in our previous class component called handleInputChange, we now have an anonymous function that updates our state for us.


**Reference:**
https://medium.freecodecamp.org/how-to-get-started-with-react-hooks-controlled-forms-826c99943b92?mkt_tok=eyJpIjoiTjJRd01tUTFObVkzWmpSaCIsInQiOiJyY25hUTFcL2VDNndHQXpXSWJ0QW54ZHpGSkhMQzhYXC9XQk5Fbkl6ekdwNGl2M1JYOTNxbUQrRVY4Y0xGSmZsXC9sb1owV2tkS1VjdU5LeDljdFhpZ1Y1Ym9pUTRzUzFYa0h1K1ZCV0k0Y1pXR0t1Y2hqaHhTaG8yamhrSmdcL0RTXC9kIn0%3D


-------------------------------------------------------------------------------
_The end._


