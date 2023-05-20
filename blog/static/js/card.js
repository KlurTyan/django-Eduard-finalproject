$(document).ready(function(){
    $.get('http://127.0.0.1:8000/api/products/', function(data,status){
        for (let i = 0; i < data.count;i++){

            const card = document.createElement('div')
            card.className = 'ProductsCard'

            const image = document.createElement('img')
            image.src = data.results[i].image

            const title = document.createElement('h1')
            title.innerHTML = data.results[i].title

            const desc = document.createElement('p')
            desc.innerHTML = data.results[i].description

            const price = document.createElement('h4')
            price.innerHTML = data.results[i].price

            card.appendChild(image)
            card.appendChild(title)
            card.appendChild(desc)
            card.appendChild(price)

            document.getElementById('card-container').appendChild(card);
        }
    })
})