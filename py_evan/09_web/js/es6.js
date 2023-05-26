let man1 = {
    name: 'evan',
    age: 32
}

let man2 = {
    hobby: 'gun',
    address: 'NYC'
}

let obj = {
    ...man1, ...man2
}

console.log(obj)

const {abs, PI} = Math
console.log(PI)

const [a, b] = 'hi'

const APP_NAME = 'online_question'
const VERSION = '1.1'
export {
    APP_NAME, VERSION
}

function say() {
    console.log('say')
}

export default say