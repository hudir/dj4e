- Class
- Method or Message
- Attribute
- Object or Instance


```js
function PartyAnimal(nam) {
    this.x = 0;
    this.name = nam;
    console.log("Build " + nam)
    this.party = function() {
        this.x += 1;
        console.log(nam +" = " + this.x)
    }
}

an = new PartyAnimal();

an.party
```