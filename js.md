JavaScript
===============================================================================

[TOC]


-------------------------------------------------------------------------------
# Snippets

## async / await

If you’re still stuck in callback hell, 2014 wants its code back. Just don’t use callbacks, unless it is absolutely necessary, for example required by a library or for performance reasons. Promises are fine, but they’re a bit awkward to use if your codebase gets bigger. My go-to solution nowadays is async / await, which makes reading and improving my code a lot cleaner. In fact, you can await every Promise in JavaScript, in case a library you’re using is returning a Promise, simply await it. In fact, async/await is just syntactical sugar around promises. To make your code work, you only need to add the async keyword in front of a function. Here’s a quick example:

```
async function getData() {
    const result = await axios.get('https://dube.io/service/ping')
    const data = result.data
    
    console.log('data', data)
    
    return data
}

getData()
```

> Note that await on the top level is not possible, you can only call an async function.
async / await was introduced with ES2017, so make sure to transpile your code.

_Reference: [JS-TIP-2019-01]_


## async control flow

Often times, it is necessary to fetch multiple datasets and do something for each of those or complete a task after all of the async calls have returned a value.

for…of

Let’s say we have a couple of Pokemon on our page, and we have to fetch detailed information about them. We do not want to wait for all calls to finish, especially when we don’t know how many there are, but we want to update our datasets as soon as we get something in return. We can use for...of to loop through an array and execute async code inside the block, the execution will be halted until each call has succeeded. It is important to note that there may be performance bottlenecks if you do something like this in your code, but it is very useful to keep in your toolset. Here is an example:

```
import axios from 'axios'

let myData = [{id: 0}, {id: 1}, {id: 2}, {id: 3}]

async function fetchData(dataSet) {
    for(entry of dataSet) {
        const result = await axios.get(`https://ironhack-pokeapi.herokuapp.com/pokemon/${entry.id}`)
        const newData = result.data
        updateData(newData)
        
        console.log(myData)
    }
}

function updateData(newData) {
    myData = myData.map(el => {
        if(el.id === newData.id) return newData
        return el
    })
}
    
fetchData(myData)
```

_Reference: [JS-TIP-2019-01]_


## Promise.all

What if you want to fetch all of the Pokemon in parallel? Since you can await all of Promises, simply use Promise.all :

```
import axios from 'axios' 

let myData = [{id: 0}, {id: 1}, {id: 2}, {id: 3}]

async function fetchData(dataSet) {
    const pokemonPromises = dataSet.map(entry => {
        return axios.get(`https://ironhack-pokeapi.herokuapp.com/pokemon/${entry.id}`)
    })

    const results = await Promise.all(pokemonPromises)
    
    results.forEach(result => {
        updateData(result.data)
    })
    
    console.log(myData) 
}

function updateData(newData) {
    myData = myData.map(el => {
        if(el.id === newData.id) return newData
        return el
    })
}
    
fetchData(myData)
```

> for...of and Promise.all were introduced with ES6+, so make sure to transpile your code.

_Reference: [JS-TIP-2019-01]_

## Destructuring & default values

Let’s return to our previous example where we do the following:
>const result = axios.get(`https://ironhack-pokeapi.herokuapp.com/pokemon/${entry.id}`)
const data = result.data

There is an easier way to do that, we can use destructuring to just take one or some of values from an object or an array. We would do it like this:
>const { data } = await axios.get(...)

We saved one line of code! Yay! You can also rename your variable:
>const { data: newData } = await axios.get(...)

Another nice trick is to give default values when destructuring. This ensures that you will never end up with undefined and you don’t have to check the variables manually.
>const { id = 5 } = {}
console.log(id) // 5

These tricks can also be used with function parameters, for example:
```
function calculate({operands = [1, 2], type = 'addition'} = {}) {
    return operands.reduce((acc, val) => {
        switch(type) {
            case 'addition':
                return acc + val
            case 'subtraction':
                return acc - val
            case 'multiplication':
                return acc * val
            case 'division':
                return acc / val
        }
    }, ['addition', 'subtraction'].includes(type) ? 0 : 1)
}

console.log(calculate()) // 3
console.log(calculate({type: 'division'})) // 0.5
console.log(calculate({operands: [2, 3, 4], type: 'multiplication'})) // 24
```

The example might seem a bit confusing at first, but take your time and play around with it. When we do not pass any values as arguments to our function, the default values are used. As soon as we start passing values, only the default values for non-existing arguments are used.

> Destructuring and default values were introduced with ES6, so make sure to transpile your code.

_Reference: [JS-TIP-2019-01]_

## Truthy & falsy values

When using default values, some of the checks for existing values will be a thing of the past. However, it is very nice to know that you can work with truthy and falsy values. This will improve your code and save you a couple of instructions, making it more eloquent. Often times I see people doing something like:

```
if(myBool === true) {
  console.log(...)
}
// OR
if(myString.length > 0) {
  console.log(...)
}
// OR
if(isNaN(myNumber)) {
  console.log(...)
}
```

All of those can be shortened to:
```
if(myBool) {
  console.log(...)
}
// OR
if(myString) {
  console.log(...)
}
// OR
if(!myNumber) {
  console.log(...)
}
```

To really take advantage of these statements, you have to understand what truthy and falsy values are. Here is a small overview:

**Falsy**
- strings with the length of 0
- the number 0
- false
- undefined
- null
- NaN

**Truthy**
- empty arrays
- •empty objects
- Everything else

>Note that when checking for truthy / falsy values, there is no explicit comparison, which equates to checking with double equal signs == and not three ===. In general, it behaves the same way but there are certain situations where you will end up with a bug. For me, it happened mostly with the number 0.

_Reference: [JS-TIP-2019-01]_


## Ternary operator
The ternary operator is very similar to the logical operator, but has three parts:
1. The comparison, which will either be falsy or truthy
2. The first return value, in case the comparison is truthy
3. The second return value, in case the comparison is falsy

Here’s an example:
```
const lang = 'German'
console.log(lang === 'German' ? 'Hallo' : 'Hello') // Hallo
console.log(lang ? 'Ja' : 'Yes') // Ja
console.log(lang === 'French' ? 'Bon soir' : 'Good evening') // Good evening
```

_Reference: [JS-TIP-2019-01]_


## Optional chaining
Have you ever had the problem of accessing a nested object property, without knowing if the object or one of the sub-properties even exists? You will probably end up with something like this:
>let data
if(myObj && myObj.firstProp && myObj.firstProp.secondProp && myObj.firstProp.secondProp.actualData) data = myObj.firstProp.secondProp.actualData

This is tedious and there’s a better way, at least a proposed way (keep reading how to enable it). It is called optional chaining and works as followed:
>const data = myObj?.firstProp?.secondProp?.actualData

I think it is an eloquent way of checking nested properties and makes the code way cleaner.

>>Currently, optional chaining is not part of the official spec, but is at stage-1 as an experimental feature. You have to add @babel/plugin-proposal-optional-chaining in your babelrc to use it.

_Reference: [JS-TIP-2019-01]_


## Class properties & binding

Binding functions in JavaScript is a common task. With the introduction of arrow functions in the ES6 spec, we now have a way to automatically bind functions to the declaration context — very useful and commonly used amongst JavaScript developers. When classes were first introduced, you could no longer really use arrow functions because class methods have to be declared in a specific way. We needed to bind functions elsewhere, for example in the constructor (best practice with React.js). I was always bugged by the workflow of first defining class methods and then binding them, it just seems ridiculous after a while. With the class property syntax, we can use arrow functions again and get the advantages of auto-binding. Arrow function can now be used inside the class. Here is an example with _increaseCount being bound:

```
class Counter extends React.Component {
    constructor(props) {
        super(props)
        this.state = { count: 0 }
    }
    
    render() {
        return(
            <div>
                <h1>{this.state.count}</h1>  
                <button onClick={this._increaseCount}>Increase Count</button>
            </div>
        )
    }
    
    _increaseCount = () => {
        this.setState({ count: this.state.count + 1 })
    }
}
```

>> Currently, class properties are not part of the official spec, but is at stage-3 as an experimental feature. You have to add @babel/plugin-proposal-class-properties in your babelrc to use it.

_Reference: [JS-TIP-2019-01]_


## var vs. let vs. const

var: 
- function scoped
- undefined when accessing a variable before it's declared

let: 
- block scoped
- ReferenceError when accessing a variable before it's declared

const:
- block scoped
- ReferenceError when accessing a variable before it's declared
- can't be reassigned (but proerties can!)

const sample:
```
const person = {
  name: 'Kim Kardashian'
}
person.name = 'Kim Kardashian West' // ✅

person = {} // ❌ Assignment to constant variable.
```


_Reference: [JS-VAR-LET-CONST]_


## ...
```
```
## ...
```
```

-------------------------------------------------------------------------------
# References

- [JS-TIP-2019-01] JavaScript Tricks 01/2019
  https://levelup.gitconnected.com/9-tricks-for-kickass-javascript-developers-in-2019-eb01dd3def2a?mkt_tok=eyJpIjoiT1RjelpERmlORE5qWlRRMiIsInQiOiJGRDRJdWs3SWdRQ1ZzUWdpdCtFVFk4M21McFNOMWRkKzJKRUkxUGdWNFRLYVJ2S3ZKd3dQUGlUQjZOWVR5SGNoUDhyMWFSTXNtY2ZMMHNJcXkwRTdHVGhrR2Z5cEVjXC9QU3czSXowaFlzNFZMK3EycUVzQjR6NWlCOXR1WGdrTGUifQ%3D%3D 


- [JS-VAR-LET-CONST] JavaScript var vs. let vs. const
  https://medium.freecodecamp.org/var-vs-let-vs-const-in-javascript-2954ae48c037?mkt_tok=eyJpIjoiT1RjelpERmlORE5qWlRRMiIsInQiOiJGRDRJdWs3SWdRQ1ZzUWdpdCtFVFk4M21McFNOMWRkKzJKRUkxUGdWNFRLYVJ2S3ZKd3dQUGlUQjZOWVR5SGNoUDhyMWFSTXNtY2ZMMHNJcXkwRTdHVGhrR2Z5cEVjXC9QU3czSXowaFlzNFZMK3EycUVzQjR6NWlCOXR1WGdrTGUifQ%3D%3D

-------------------------------------------------------------------------------
_The end._

